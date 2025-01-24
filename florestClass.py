import pygame
import os

class Florest:
    def __init__(self):
        # Configuração dos diretórios
        diretorio_main_florest = os.path.dirname(__file__)
        diretorio_assets = os.path.join(diretorio_main_florest, 'assets')
        diretorio_mapas = os.path.join(diretorio_assets, 'mapas')
        diretorio_floresta = os.path.join(diretorio_mapas, 'floresta')

        # Carregar imagens
        self.background = pygame.image.load(os.path.join(diretorio_floresta, 'backFloresta.png'))
        self.plataforma_p = pygame.image.load(os.path.join(diretorio_floresta, 'groundFloresta.png'))
        self.plataforma1 = pygame.image.load(os.path.join(diretorio_floresta, 'plataformaFloresta.png'))
        self.plataforma2 = pygame.image.load(os.path.join(diretorio_floresta, 'plataformaFloresta.png'))
        self.plataforma3 = pygame.image.load(os.path.join(diretorio_floresta, 'plataformaFloresta.png'))

        # Definir plataformas como retângulos
        self.plataformas = [
            pygame.Rect(140, 490, 1059, 137),  # Plataforma P (posição x, y, largura, altura)
            pygame.Rect(320, 319, 214, 80),
            pygame.Rect(780,319,214,80),
            pygame.Rect(560,200,214,80)   # Plataforma 2
        ]

    def draw(self, surface):
        """
        Desenha o cenário e as plataformas na superfície fornecida.
        """
        # Desenhar o fundo
        surface.blit(self.background, (0, 0))

        # Desenhar as plataformas
        surface.blit(self.plataforma_p, (140, 490))
        surface.blit(self.plataforma1, (320, 319))
        surface.blit(self.plataforma2,(780,319))
        surface.blit(self.plataforma3,(560,200))

        # Retorna informações sobre as plataformas
        return self.plataformas
