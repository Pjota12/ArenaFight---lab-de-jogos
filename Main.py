from PPlay.window import Window
from PPlay.keyboard import Keyboard
import pygame
import os
from menu import haddleMenuEvents
from controls import drawControls
from options import HaddleOptionsEvents
from ChampSelect import drawChampionsSelector
from GameLoop import run_game_loop
from winnerScream import drawWinnerScream

pygame.init()
pygame.mixer.init()

# Criação da janela
window = Window(1400, 750)
window.set_title("🥊 MENU 🥊")

# Criação de uma superfície do Pygame para desenhar
pygame_surface = pygame.display.set_mode((1400, 750))  # Mesmo tamanho da janela PPlay

# Inicialização do teclado e estado do jogo
keyboard = Keyboard()
estado = "menu"
sair = False

#diretorio
diretorio = os.path.dirname(__file__)
caminho_musica = os.path.join(diretorio, 'assets', 'main.wav')

pygame.mixer.music.load(caminho_musica)
pygame.mixer.music.set_volume(0.5)
musica_tocando = False
#options:
drawSquare = False
squareX = 0
retangleX = 205
retangleMODO = 380
tempo = 3
mapa = 1
modo = 0

#selector
p1x = 18
p1y = 243
p2x = 700
p2y = 240
p1 = 1
p2 = 1

#controlador de game loop
game_estage = 0
winner = ''

#controlador da musica
isSom = False

# Função para retornar ao menu
def returnMenu():
    global estado
    if keyboard.key_pressed("ESCAPE") and estado != "menu":
        estado = "menu"

# Loop principal do jogo
while not sair:
    returnMenu()
    
    if game_estage == 0 and not musica_tocando:
        pygame.mixer.music.play(-1)  # Toca a música em loop
        musica_tocando = True  # Atualiza o estado da música
    elif game_estage != 0 and musica_tocando:
        pygame.mixer.music.stop()  # Para a música
        musica_tocando = False  # Atualiza o estado da música

    # Controle de estados
    if estado == "menu":
        estado, sair = haddleMenuEvents(window)
        isSom = False
    elif estado == "jogando":
        if game_estage == 0:
            p1, p2, p1x, p1y, p2x, p2y,game_estage,isSom = drawChampionsSelector(pygame_surface, p1, p2, p1x, p1y, p2x, p2y,game_estage,isSom)
        elif game_estage == 1:
            isSom = False
            game_estage,winner = run_game_loop(pygame_surface,p1,p2,tempo,mapa,modo)
        elif game_estage == 2:
            game_estage,estado,winner = drawWinnerScream(pygame_surface,p1,p2,winner,game_estage,estado)
    elif estado == "controles":
        drawControls(pygame_surface)  # Passa a superfície do Pygame para desenhar
    elif estado == "opcoes":
        squareX,retangleX,retangleMODO,drawSquare,tempo,mapa,modo = HaddleOptionsEvents(window,squareX,drawSquare,retangleX,retangleMODO,tempo,mapa,modo)
    # Atualiza a superfície do Pygame na tela
    pygame.display.flip()

    # Atualiza o frame da janela (PPlay)
    window.update()


