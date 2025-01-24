import pygame
from pygame.locals import*
from PPlay.gameimage import*
from PPlay.mouse import*
import os

pygame.mixer.init()
class Ayla(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        
        # Adicionando imagens da animação
        for i in range(1, 8):
            sprite = pygame.image.load(f'./assets/Personagens/Ayla/PNG/01_idle/idle_{i}.png')
            self.sprites.append(sprite)
        
        self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 5, 128 * 5))

        self.rect = self.image.get_rect()
    
    def update(self):
        # Atualiza o frame da animação
        self.atual += 0.30
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 5, 128 * 5))

class Wander(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        
        # Adicionando imagens da animação
        for i in range(1, 8):
            sprite = pygame.image.load(f'./assets/Personagens/wander/PNG/idle/idle_{i}.png')
            self.sprites.append(sprite)
        
        self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 5, 128 * 5))

        self.rect = self.image.get_rect()
    
    def update(self):
        # Atualiza o frame da animação
        self.atual += 0.30
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 5, 128 * 5))

class Drax(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        
        # Adicionando imagens da animação
        for i in range(1, 8):
            sprite = pygame.image.load(f'./assets/Personagens/Drax/PNG/PNG/idle/idle_{i}.png')
            self.sprites.append(sprite)
        
        self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 5, 128 * 5))

        self.rect = self.image.get_rect()
    
    def update(self):
        # Atualiza o frame da animação
        self.atual += 0.30
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 5, 128 * 5))

class Dayla(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        
        # Adicionando imagens da animação
        for i in range(1, 6):
            sprite = pygame.image.load(f'./assets/Personagens/dayla/PNG/01_idle/01_idle_{i}.png')
            self.sprites.append(sprite)
        
        self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 5, 128 * 5))

        self.rect = self.image.get_rect()
    
    def update(self):
        # Atualiza o frame da animação
        self.atual += 0.30
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 5, 128 * 5))

# Criar o grupo de sprites
ayla = Ayla()
drax = Drax()
dayla = Dayla()
wander = Wander()

diretorio = os.path.dirname(__file__)
caminho_musica = os.path.join(diretorio, 'assets', 'select_your_character.wav')

som1 = pygame.mixer.Sound(caminho_musica)
som1.set_volume(0.8)


def drawChampionsSelector(surface, p1, p2, p1x, p1y, p2x, p2y,game_estage,som):
    global som1
    mouse = Mouse()
    p1square = GameImage("./assets/seletorP1.png")
    p2square = GameImage("./assets/seletorP2.png")

    if not som:
        som1.play()
        som = True

    

    # Carregar e desenhar o fundo
    background = pygame.image.load("./assets/backSelector.png").convert()
    surface.blit(background, (0, 0))

    # Atualizar posição dos seletores
    p1square.x = p1x
    p1square.y = p1y
    p2square.x = p2x
    p2square.y = p2y

    # Desenhar os seletores
    p1square.draw()
    p2square.draw()

    # Inicializar sprites
    wander.update()
    ayla.update()
    drax.update()
    dayla.update()

    # Desenhar os personagens
    if p1 == 1:
        wander.rect.topleft = (-200, -150)
        surface.blit(wander.image, wander.rect.topleft)
    elif p1 == 2:
        dayla.rect.topleft = (-200, -120)
        surface.blit(dayla.image, dayla.rect.topleft)
    elif p1 == 3:
        ayla.rect.topleft = (-200, -150)
        surface.blit(ayla.image, ayla.rect.topleft)
    elif p1 == 4:
        drax.rect.topleft = (-200, -150)
        surface.blit(drax.image, drax.rect.topleft)

    if p2 == 1:
        wander.rect.topleft = (475, -150)
        surface.blit(wander.image, wander.rect.topleft)
    elif p2 == 2:
        dayla.rect.topleft = (475, -120)
        surface.blit(dayla.image, dayla.rect.topleft)
    elif p2 == 3:
        ayla.rect.topleft = (475, -150)
        surface.blit(ayla.image, ayla.rect.topleft)
    elif p2 == 4:
        drax.rect.topleft = (475, -150)
        surface.blit(drax.image, drax.rect.topleft)

    # Lógica de seleção de personagem para o Player 1
    if mouse.is_over_area([26, 252], [146, 369]) and mouse.is_button_pressed(1):
        p1 = 1
        p1x = 18
        p1y = 243
    elif mouse.is_over_area([220, 252], [340, 369]) and mouse.is_button_pressed(1):
        p1 = 2
        p1x = 210
        p1y = 243
    elif mouse.is_over_area([26, 428], [146, 538]) and mouse.is_button_pressed(1):
        p1 = 3
        p1x = 17
        p1y = 410
    elif mouse.is_over_area([220, 428], [340, 538]) and mouse.is_button_pressed(1):
        p1 = 4
        p1x = 210
        p1y = 410

    # Lógica de seleção de personagem para o Player 2
    if mouse.is_over_area([707, 252], [832, 370]) and mouse.is_button_pressed(1):
        p2 = 1
        p2x = 700
        p2y = 240
    elif mouse.is_over_area([908, 252], [1025, 370]) and mouse.is_button_pressed(1):
        p2 = 2
        p2x = 898
        p2y = 240
    elif mouse.is_over_area([707, 428], [832, 538]) and mouse.is_button_pressed(1):
        p2 = 3
        p2x = 701
        p2y = 408
    elif mouse.is_over_area([908, 428], [1025, 538]) and mouse.is_button_pressed(1):
        p2 = 4
        p2x = 898
        p2y = 408
    
    if mouse.is_over_area([1037,658],[1338,719]) and mouse.is_button_pressed(1):
        game_estage = 1

    return p1, p2, p1x, p1y, p2x, p2y,game_estage,som




    
