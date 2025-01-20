from PPlay.gameimage import GameImage
from PPlay.mouse import Mouse

def drawMenu(window):
    background = GameImage("./assets/backgroundArena.png")
    logo = GameImage("./assets/logo.png")
    play = GameImage("./assets/jogar.png")
    options = GameImage("./assets/opcoes.png")
    controls = GameImage("./assets/controles.png")
    leave = GameImage("./assets/sair.png")

    # Centralizar e posicionar os elementos
    logo.x = window.width / 2 - logo.width / 2
    logo.y = 15

    play.x = window.width / 2 - play.width / 2
    play.y = window.height / 2.9

    options.x = window.width / 2 - options.width / 2
    options.y = window.height / 2

    controls.x = window.width / 2 - controls.width / 2
    controls.y = window.height / 1.5

    leave.x = window.width / 2 - leave.width / 2
    leave.y = window.height / 1.2

    # Desenhar os elementos na tela
    background.draw()
    logo.draw()
    play.draw()
    options.draw()
    controls.draw()
    leave.draw()

    # Retornar os botões para verificação de eventos
    return play, options, controls, leave


def haddleMenuEvents(window):
    mouse = Mouse()

    # Obter os botões do menu
    play, options, controls, leave = drawMenu(window)

    # Verificar cliques nos botões
    if mouse.is_over_area([play.x, play.y], [play.x + play.width, play.y + play.height]) and mouse.is_button_pressed(1):
        return "jogando", False

    if mouse.is_over_area([options.x, options.y], [options.x + options.width, options.y + options.height]) and mouse.is_button_pressed(1):
        return "opcoes", False

    if mouse.is_over_area([controls.x, controls.y], [controls.x + controls.width, controls.y + controls.height]) and mouse.is_button_pressed(1):
        return "controles", False

    if mouse.is_over_area([leave.x, leave.y], [leave.x + leave.width, leave.y + leave.height]) and mouse.is_button_pressed(1):
        return "menu", True  # Sinalizar que o jogo deve encerrar

    return "menu", False




