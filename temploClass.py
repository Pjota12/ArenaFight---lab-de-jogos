import pygame
import os

class Templo:
    def __init__(self):
        # Configuração dos diretórios
        diretorio_main_templo = os.path.dirname(__file__)
        diretorio_assets = os.path.join(diretorio_main_templo, 'assets')
        diretorio_mapas = os.path.join(diretorio_assets, 'mapas')
        diretorio_templo = os.path.join(diretorio_mapas, 'templo')

        # Carregar imagens
        self.background = pygame.image.load(os.path.join(diretorio_templo, 'backTemplo.png'))
        self.plataforma_p = pygame.image.load(os.path.join(diretorio_templo, 'groundTemplo.png'))
        self.plataforma1 = pygame.image.load(os.path.join(diretorio_templo, 'ground2.png'))
        self.plataforma2 = pygame.image.load(os.path.join(diretorio_templo, 'ground2.png'))

        # Definir plataformas como retângulos
        self.plataformas = [
            pygame.Rect(240, 490, 791, 75),  # Plataforma P (posição x, y, largura, altura)
            pygame.Rect(360, 319, 177, 76),
            pygame.Rect(720,319,177,76)   # Plataforma 2
        ]

    def draw(self, surface):
        """
        Desenha o cenário e as plataformas na superfície fornecida.
        """
        # Desenhar o fundo
        surface.blit(self.background, (0, 0))

        # Desenhar as plataformas
        surface.blit(self.plataforma_p, (240, 490))
        surface.blit(self.plataforma1, (360, 319))
        surface.blit(self.plataforma2,(720,319))

        # Retorna informações sobre as plataformas
        return self.plataformas
