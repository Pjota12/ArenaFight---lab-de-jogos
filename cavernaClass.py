import pygame
import os

class Caverna:
    def __init__(self):
        # Configuração dos diretórios
        diretorio_main_caverna = os.path.dirname(__file__)
        diretorio_assets = os.path.join(diretorio_main_caverna, 'assets')
        diretorio_mapas = os.path.join(diretorio_assets, 'mapas')
        diretorio_caverna = os.path.join(diretorio_mapas, 'caverna')

        # Carregar imagens
        self.background = pygame.image.load(os.path.join(diretorio_caverna, 'backCaverna.png'))
        self.plataforma_p = pygame.image.load(os.path.join(diretorio_caverna, 'plataformaCaverna.png'))
        self.plataforma2 = pygame.image.load(os.path.join(diretorio_caverna, 'plataforma2Caverna.png'))

        # Definir plataformas como retângulos
        self.plataformas = [
            pygame.Rect(220, 490, 881, 207),  # Plataforma P (posição x, y, largura, altura)
            pygame.Rect(510, 319, 327, 59)   # Plataforma 2
        ]

    def draw(self, surface):
        """
        Desenha o cenário e as plataformas na superfície fornecida.
        """
        # Desenhar o fundo
        surface.blit(self.background, (0, 0))

        # Desenhar as plataformas
        surface.blit(self.plataforma_p, (220, 490))
        surface.blit(self.plataforma2, (510, 319))

        # Retorna informações sobre as plataformas
        return self.plataformas


