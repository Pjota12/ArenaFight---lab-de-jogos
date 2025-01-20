import pygame
from pygame.locals import *
from PPlay.gameimage import *

pygame.init()

class Walk(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        
        # Adicionando imagens da animação
        for i in range(1, 9):
            sprite = pygame.image.load(f'./assets/Personagens/Drax/PNG/PNG/run/run_{i}.png')
            self.sprites.append(sprite)
        
        self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 2.5, 128 * 2.5))

        self.rect = self.image.get_rect()
        self.rect.topleft = -110,-75
    
    def update(self):
        # Atualiza o frame da animação
        self.atual += 0.30
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 2.5, 128 * 2.5))

class SuperAtack(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        for i in range(1,15):
            sprites = pygame.image.load(f'./assets/Personagens/Drax/PNG/PNG/sp_atk/sp_atk_{i}.png')
            self.sprites.append(sprites)
        
        self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 2.5, 128 * 2.5))

        self.rect = self.image.get_rect()
        self.rect.topleft = -110,285

    def update(self):

        self.atual += 0.30

        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 2.5, 128 * 2.5))

class Atack1(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        for i in range(1,6):
            sprites = pygame.image.load(f'./assets/Personagens/dayla/PNG/07_1_atk/07_1_atk_{i}.png')
            self.sprites.append(sprites)
        
        self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 2.5, 128 * 2.5))

        self.rect = self.image.get_rect()
        self.rect.topleft = 300,-115

    def update(self):

        self.atual += 0.30

        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 2.5, 128 * 2.5))

class Atack2(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        for i in range(1,21):
            sprites = pygame.image.load(f'./assets/Personagens/Ayla/PNG/08_2_atk/2_atk_{i}.png')
            self.sprites.append(sprites)
        
        self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 2.5, 128 * 2.5))

        self.rect = self.image.get_rect()
        self.rect.topleft = 300,100

    def update(self):

        self.atual += 0.30

        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 2.5, 128 * 2.5))

class Atack3(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        for i in range(1,26):
            sprites = pygame.image.load(f'./assets/Personagens/wander/PNG/3_atk/3_atk_{i}.png')
            self.sprites.append(sprites)
        
        self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 2.5, 128 * 2.5))

        self.rect = self.image.get_rect()
        self.rect.topleft = 300,325

    def update(self):

        self.atual += 0.30

        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 2.5, 128 * 2.5))

class Block (pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        for i in range(1,12):
            sprites = pygame.image.load(f'./assets/Personagens/Ayla/PNG/12_defend/defend_{i}.png')
            self.sprites.append(sprites)
        
        self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 2.5, 128 * 2.5))

        self.rect = self.image.get_rect()
        self.rect.topleft = 675,100

    def update(self):

        self.atual += 0.30

        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (288 * 2.5, 128 * 2.5))

# Criar o grupo de sprites
all_sprites = pygame.sprite.Group()
walk = Walk()
superAtack = SuperAtack()
atack1 = Atack1()
atack2 = Atack2()
atack3 = Atack3()
block = Block()
all_sprites.add(walk)
all_sprites.add(superAtack)
all_sprites.add(atack1)
all_sprites.add(atack2)
all_sprites.add(atack3)
all_sprites.add(block)


def drawControls(surface):
    """
    Função para desenhar a tela de controles.
    :param surface: superfície do Pygame onde os elementos serão desenhados.
    """
    # Carregar e desenhar o fundo
    background = pygame.image.load("./assets/backControls.png").convert()
    surface.blit(background, (0, 0))

    # Desenhar sprites
    all_sprites.draw(surface)
    all_sprites.update()

