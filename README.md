# TicTacToe
Python Pygame TicTacToe

![TicTacToe](screenshot/1.jpg "TicTacToe")

# Jogo da Velha em Python com Pygame

## Descrição
Este projeto implementa um clássico jogo da velha utilizando a biblioteca Pygame. O jogo permite que um jogador humano enfrente um adversário humano(Player vs Player).

## Como Jogar
1. **Instale as dependências:** Certifique-se de ter o Python e a biblioteca Pygame instalados. Você pode instalar o Pygame usando o comando `pip install pygame`.
2. **Execute o jogo:** Rode o script principal do seu projeto.
3. **Clique nas células:** Clique com o mouse nas células vazias do tabuleiro para fazer sua jogada.
4. **Verifique o vencedor:** O jogo irá indicar o vencedor ou se houve empate.

## Características
* **Interface gráfica:** Utiliza o Pygame para criar uma interface visual intuitiva.
* **Mecânica do jogo:** Implementa as regras tradicionais do jogo da velha.
* **Inteligência artificial básica:** O computador realiza jogadas aleatórias.
* **Verificação de vitória:** Detecta automaticamente quando há um vencedor ou empate.

## Estrutura do Código
* **Classes:**
  * `TicTacToe`: Controla a lógica principal do jogo, como o tabuleiro, as jogadas e a verificação de vitória.
  * `Game`: Cria a janela do jogo, gerencia eventos e o loop principal.
* **Módulos:**
  * `pygame`: Utilizado para criar a interface gráfica e lidar com eventos.
  * `sys`: Utilizado para sair do jogo quando necessário.
  * `random`: Utilizado para gerar números aleatórios para as jogadas do computador.

## Contribuições
Contribuições são bem-vindas! Se você encontrar algum bug ou tiver alguma sugestão, por favor, abra um issue ou faça um pull request.

## Próximos Passos
* **Melhorar a IA:** Implementar algoritmos de IA mais sofisticados para tornar o jogo mais desafiador.
* **Adicionar modos de jogo:** Permitir que dois jogadores humanos joguem um contra o outro.
* **Personalização:** Adicionar opções para personalizar a aparência do jogo.

## Licença
[MIT License Copyright (c) 2022 StanislavPetrovV]

## Autores
* [StanislavPetrovV/ Thales Augusto] - Desenvolvedor principal/ Código adaptado

**Dicas:**

* **Agradecimentos:** Agradeço a todos que tenham contribuído para o projeto.


Estrutura Geral:
Classes: O código utiliza duas classes principais: TicTacToe e Game.
TicTacToe: Controla toda a lógica do jogo, como o tabuleiro, as jogadas, a verificação de vitória e o desenho dos elementos na tela.
Game: Cria a janela do jogo, controla o loop principal e gerencia eventos como o clique do mouse e o pressionamento de teclas.
Módulos: Importa os módulos pygame, sys e random.
pygame: Biblioteca para criar jogos em Python.
sys: Módulo para interagir com o interpretador Python.
random: Módulo para gerar números aleatórios.
Explicação Detalhada:
Inicialização:
Variáveis: Define o tamanho da janela, o tamanho de cada célula, uma matriz para representar o tabuleiro, um dicionário para armazenar as imagens, e outras variáveis para controlar o jogo.
Imagens: Carrega as imagens do tabuleiro, do "O" e do "X".
Lógica do Jogo:
Verificação de Vitória: Verifica se há três símbolos iguais em uma linha, coluna ou diagonal.
Jogadas: Atualiza o estado do tabuleiro de acordo com a jogada do jogador.
Desenho: Desenha o tabuleiro, os símbolos e a mensagem de vitória na tela.
Loop Principal:
Eventos: Verifica os eventos do teclado e do mouse.
Atualização: Atualiza o estado do jogo e a tela.
