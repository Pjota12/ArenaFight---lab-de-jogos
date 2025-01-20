from PPlay.gameimage import *
from PPlay.mouse import *

def HaddleOptionsEvents(window, squareX,drawSquare,retangleX,rectangleModox,tempo,mapa,modo):
    # Inicialização
    mouse = Mouse()

    # Desenhar opções
    background = GameImage("./assets/backOptions.png")
    square = GameImage("./assets/selectorSquare.png")
    rectangle = GameImage("./assets/selectorRetangular.png")
    rectangleMODO = GameImage("./assets/selectorModo.png")
    

    rectangle.x = retangleX
    rectangle.y = 370

    rectangleMODO.x = rectangleModox
    rectangleMODO.y = 600

    background.draw()

    if drawSquare:
        square.x = squareX
        square.y = 155
        square.draw()
    
    rectangle.draw()
    rectangleMODO.draw()

    

    # Verificar cliques nas áreas definidas
    if mouse.is_over_area([378, 173], [469, 250]) and mouse.is_button_pressed(1):
        squareX = 364
        drawSquare = True
        tempo = 3
    elif mouse.is_over_area([646, 173], [735, 250]) and mouse.is_button_pressed(1):
        squareX = 632
        drawSquare = True
        tempo = 5
    elif mouse.is_over_area([910, 173], [1004, 250]) and mouse.is_button_pressed(1):
        squareX = 900
        drawSquare = True
        tempo = 9
    
    if mouse.is_over_area([218, 376], [423, 472]) and mouse.is_button_pressed(1):
        retangleX = 205
        mapa = 1
    elif mouse.is_over_area([598, 376], [802, 472]) and mouse.is_button_pressed(1):
        retangleX = 583
        mapa = 2
    elif mouse.is_over_area([978, 376], [1183, 472]) and mouse.is_button_pressed(1):
        retangleX = 963
        mapa = 3
    
    if mouse.is_over_area([410, 618], [653, 670]) and mouse.is_button_pressed(1):
        rectangleModox = 380
        modo = 0
    elif mouse.is_over_area([842, 618], [996, 670]) and mouse.is_button_pressed(1):
        rectangleModox = 768
        modo = 1
    
    
    # Atualizar a tela
    window.update()

    return squareX,retangleX,rectangleModox,drawSquare,tempo,mapa,modo


    