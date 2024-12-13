import pygame as pg
import sys
from random import randint

WIN_SIZE = 900
CELL_SIZE = WIN_SIZE // 3
INF = float('inf')
vec2 = pg.math.Vector2
CELL_CENTER = vec2(CELL_SIZE / 2)


class TicTacToe:
    """
    Esta classe gerencia a lógica principal do jogo da velha, incluindo:
        - Representação e manipulação do tabuleiro
        - Vez dos jogadores e estado do jogo
        - Detecção de vitória
        - Desenho dos elementos na tela
    """

    def __init__(self, game):
        """
            Inicializa a instância de TicTacToe com uma referência ao objeto Game.

            Args:
                game (Game): O objeto Game que gerencia o loop principal e a janela do jogo.
        """

        # Armazena a referência ao objeto Game para interagir com a janela e loop principal
        self.game = game

        # Carrega e dimensiona a imagem do campo de jogo
        self.field_image = self.get_scaled_image(path='resources/field.png', res=[WIN_SIZE] * 2)
        # Caminho: resources/field.png (supondo que a imagem esteja na pasta resources)
        # Resultado: Imagem dimensionada para o tamanho da janela do jogo (WIN_SIZE x WIN_SIZE)

        # Carrega e dimensiona a imagem da marca O
        self.O_image = self.get_scaled_image(path='resources/o.png', res=[CELL_SIZE] * 2)
        # Caminho: resources/o.png (supondo que a imagem esteja na pasta resources)
        # Resultado: Imagem dimensionada para o tamanho de uma célula (CELL_SIZE x CELL_SIZE)

        # Carrega e dimensiona a imagem da marca X
        self.X_image = self.get_scaled_image(path='resources/x.png', res=[CELL_SIZE] * 2)
        # Caminho: resources/x.png (supondo que a imagem esteja na pasta resources)
        # Resultado: Imagem dimensionada para o tamanho de uma célula (CELL_SIZE x CELL_SIZE)

        # Inicializa o tabuleiro do jogo com valores INF (representando células vazias)
        self.game_array = [[INF, INF, INF],
                           [INF, INF, INF],
                           [INF, INF, INF]]

        # Define o jogador inicial aleatoriamente (0 ou 1)
        self.player = randint(0, 1)
        # randint(0, 1) gera um número inteiro aleatório entre 0 e 1

        # Cria um array contendo as combinações de índices para verificar linhas vitoriosas
        self.line_indices_array = [[(0, 0), (0, 1), (0, 2)],
                                   [(1, 0), (1, 1), (1, 2)],
                                   [(2, 0), (2, 1), (2, 2)],
                                   [(0, 0), (1, 0), (2, 0)],
                                   [(0, 1), (1, 1), (2, 1)],
                                   [(0, 2), (1, 2), (2, 2)],
                                   [(0, 0), (1, 1), (2, 2)],
                                   [(0, 2), (1, 1), (2, 0)]]

        # Inicializa o vencedor como None (sem vencedor no início do jogo)
        self.winner = None

        # Inicializa o contador de jogadas como 0
        self.game_steps = 0

        # Carrega uma fonte para exibir texto na tela (ajustada ao tamanho da célula)
        self.font = pg.font.SysFont('Verdana', CELL_SIZE // 4, True)

    def check_winner(self):
        """
        Verifica se há uma linha vencedora (3 Xs ou 3 Os) no tabuleiro.

        Atualiza o atributo self.winner se um vencedor for encontrado.
        Também calcula as coordenadas da linha vencedora para desenhar uma linha.
        """
        for line_indices in self.line_indices_array:
            sum_line = sum([self.game_array[i][j] for i, j in line_indices])
            if sum_line in {0, 3}:
                self.winner = 'XO'[sum_line == 0]
                self.winner_line = [vec2(line_indices[0][::-1]) * CELL_SIZE + CELL_CENTER,
                                    vec2(line_indices[2][::-1]) * CELL_SIZE + CELL_CENTER]

    def run_game_process(self):
        """
        Handles user input (mouse clicks) and updates the game state accordingly.
        Gerencia a lógica principal do jogo, atualizando o estado do jogo com base nas ações do jogador.

        1. Obtém as coordenadas da célula clicada pelo jogador.
        2. Verifica se a célula está vazia e se o jogo ainda não acabou.
        3. Se a célula estiver válida, atualiza o estado do tabuleiro com a marca do jogador atual.
        4. Alterna para o próximo jogador.
        5. Incrementa o contador de jogadas.
        6. Verifica se há um vencedor após a jogada.
        """

        # Obtém as coordenadas da célula clicada pelo jogador (convertido para índices do tabuleiro)
        current_cell = vec2(pg.mouse.get_pos()) // CELL_SIZE
        col, row = map(int, current_cell)

        # Verifica se o botão esquerdo do mouse foi pressionado
        left_click = pg.mouse.get_pressed()[0]

        # Processa a jogada apenas se o clique for válido (botão esquerdo pressionado, célula vazia e nenhum vencedor)
        if left_click and self.game_array[row][col] == INF and not self.winner:
            # Atualiza o tabuleiro com a marca do jogador atual
            self.game_array[row][col] = self.player

            # Alterna para o próximo jogador
            self.player = not self.player

            # Incrementa o contador de jogadas
            self.game_steps += 1

            # Verifica se há um vencedor após a jogada
            self.check_winner()

    # Percorre cada linha e célula do tabuleiro
    def draw_objects(self):
        for y, row in enumerate(self.game_array):
            for x, obj in enumerate(row):
                # Verifica se a célula não está vazia (INF)
                if obj != INF:
                    # Desenha a imagem X ou O na célula correspondente
                    self.game.screen.blit(self.X_image if obj else self.O_image, vec2(x, y) * CELL_SIZE)

    # Função que desenha linha da vitória
    def draw_winner(self):
        # Verifica se há um vencedor
        if self.winner:
            pg.draw.line(self.game.screen, 'red', *self.winner_line, CELL_SIZE // 8)
            label = self.font.render(f'Player "{self.winner}" wins!', True, 'white', 'black')
            self.game.screen.blit(label, (WIN_SIZE // 2 - label.get_width() // 2, WIN_SIZE // 4))

    # Desenha o fundo do jogo e os objetos
    def draw(self):
        # Desenha o fundo do jogo
        self.game.screen.blit(self.field_image, (0, 0))

        # Desenha os objetos X e O no tabuleiro
        self.draw_objects()

        # Desenha a linha vencedora, se houver
        self.draw_winner()

    @staticmethod
    def get_scaled_image(path, res):
        # Carrega a imagem a partir do caminho especificado
        img = pg.image.load(path)

        # Redimensiona a imagem para o tamanho desejado (res)
        return pg.transform.smoothscale(img, res)

    def print_caption(self):

        # Define a legenda padrão com o turno do jogador atual
        pg.display.set_caption(f'Player "{"OX"[self.player]}" turn!')

        # Verifica se há um vencedor e atualiza a legenda com mensagem de vitória e instrução para reiniciar
        if self.winner:
            pg.display.set_caption(f'Player "{self.winner}" wins! Press Space to Restart')

        # Verifica se o jogo empatou e atualiza envia mensagem de empate e instrução para reiniciar pressionando espaço
        elif self.game_steps == 9:
            pg.display.set_caption(f'Game Over! Press Space to Restart')

    def run(self):
        # Atualiza a legenda da janela
        self.print_caption()

        # Desenha todos os elementos do jogo na tela
        self.draw()

        # Processa a jogada do usuário
        self.run_game_process()


class Game:
    """
       Gerencia o loop principal do jogo, a criação da janela e o tratamento de eventos.
    """
    def __init__(self):
        """
         Inicializa o objeto Game:
             - Inicializa o Pygame.
             - Cria a janela do jogo.
             - Cria um objeto de relógio para controlar a taxa de quadros.
             - Cria uma instância de TicTacToe.
         """
        pg.init()
        self.screen = pg.display.set_mode([WIN_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.tic_tac_toe = TicTacToe(self)

    def new_game(self):
        """
        Inicia um novo jogo, criando uma nova instância de TicTacToe.
        """
        self.tic_tac_toe = TicTacToe(self)

    def check_events(self):
        """
        Verifica os eventos do teclado e do mouse:
            - Encerra o jogo se o botão de fechar for clicado.
            - Reinicia o jogo se a barra de espaço for pressionada.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.new_game()

    def run(self):
        """
        Loop principal do jogo:
            - Executa a lógica do jogo TicTacToe.
            - Verifica eventos.
            - Atualiza a tela.
            - Controla a taxa de quadros.
        """
        while True:
            self.tic_tac_toe.run()  # Executa uma iteração da lógica do jogo
            self.check_events()  # Verifica se há eventos (clique do mouse, teclado, etc.)
            pg.display.update()  # Atualiza a tela com as mudanças
            self.clock.tick(60)  # Limita a taxa de quadros a 60 FPS


if __name__ == '__main__':
    game = Game()
    game.run()
