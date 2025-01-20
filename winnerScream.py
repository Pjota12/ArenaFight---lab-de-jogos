import pygame
from pygame.locals import*
from PPlay.gameimage import*
from PPlay.mouse import*
import os

class Ayla(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        diretorio_aylaClass = os.path.dirname(__file__)
        diretorio_assets = os.path.join(diretorio_aylaClass, 'assets')
        diretorio_personagens = os.path.join(diretorio_assets, 'Personagens')
        diretorio_ayla = os.path.join(diretorio_personagens, 'Ayla')

        # Carregar o spritesheet
        self.sprite_sheet = pygame.image.load(os.path.join(diretorio_ayla, 'AylaSpriteSheet.png')).convert_alpha()
        self.sprites = {action: [] for action in [
            'idle','die'
        ]}

        self.load_sprites('idle', start_row=0, num_frames=8)
        self.load_sprites('die',start_row=14,num_frames=16)
        
        self.current_action = 'idle'
        self.index = 0
        self.image = self.sprites[self.current_action][self.index]
        self.flip = False
        self.rect = self.image.get_rect()
        self.rect.center = (300, 150)
        self.frame_count = 0  # Contador de frames
        self.frame_delay = 9  # Número de updates para trocar o frame
    
    def load_sprites(self, action, start_row, num_frames):
        for i in range(num_frames):
            img = self.sprite_sheet.subsurface((288 * i, 128 * start_row), (288, 128))
            img = pygame.transform.scale(img, (288 * 6, 128 * 6))
            self.sprites[action].append(img)
    
    def change_action(self, action):
        if action != self.current_action:
            self.current_action = action
            self.index = 0

    def update(self):
        """
        Atualiza o frame da animação e aplica o flip na imagem se necessário.
        """
        self.frame_count += 1

        # Altera o frame da animação após atingir o frame_delay
        if self.frame_count >= self.frame_delay:
            self.frame_count = 0
            self.index = (self.index + 1) % len(self.sprites[self.current_action])
            self.image = self.sprites[self.current_action][self.index]

        # Aplica o flip na imagem se necessário
        if self.flip:
            self.image = pygame.transform.flip(self.sprites[self.current_action][self.index], True, False)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Wander(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        diretorio_wanderClass = os.path.dirname(__file__)
        diretorio_assets = os.path.join(diretorio_wanderClass, 'assets')
        diretorio_personagens = os.path.join(diretorio_assets, 'Personagens')
        diretorio_wander = os.path.join(diretorio_personagens, 'wander')

        # Carregar o spritesheet
        self.sprite_sheet = pygame.image.load(os.path.join(diretorio_wander, 'wanderSpriteSheet.png')).convert_alpha()
        self.sprites = {action: [] for action in [
            'idle','die'
        ]}

        self.load_sprites('idle', start_row=0, num_frames=8)
        self.load_sprites('die',start_row=12,num_frames=19)
        
        self.current_action = 'idle'
        self.index = 0
        self.image = self.sprites[self.current_action][self.index]
        self.flip = False
        self.rect = self.image.get_rect()
        self.rect.center = (1150, 370)
        self.frame_count = 0  # Contador de frames
        self.frame_delay = 9  # Número de updates para trocar o frame
    
    def load_sprites(self, action, start_row, num_frames):
        for i in range(num_frames):
            img = self.sprite_sheet.subsurface((288 * i, 128 * start_row), (288, 128))
            img = pygame.transform.scale(img, (288 * 6, 128 * 6))
            self.sprites[action].append(img)
    
    def change_action(self, action):
        if action != self.current_action:
            self.current_action = action
            self.index = 0

    def update(self):
        """
        Atualiza o frame da animação e aplica o flip na imagem se necessário.
        """
        self.frame_count += 1
        if self.frame_count >= self.frame_delay:
            self.frame_count = 0
            self.index = (self.index + 1) % len(self.sprites[self.current_action])
            self.image = self.sprites[self.current_action][self.index]

        # Aplica o flip na imagem se necessário
        if self.flip:
            self.image = pygame.transform.flip(self.sprites[self.current_action][self.index], True, False)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Drax(pygame.sprite.Sprite):
   def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        diretorio_draxClass = os.path.dirname(__file__)
        diretorio_assets = os.path.join(diretorio_draxClass, 'assets')
        diretorio_personagens = os.path.join(diretorio_assets, 'Personagens')
        diretorio_Drax = os.path.join(diretorio_personagens, 'Drax')

        # Carregar o spritesheet
        self.sprite_sheet = pygame.image.load(os.path.join(diretorio_Drax, 'draxSpriteSheet.png')).convert_alpha()
        self.sprites = {action: [] for action in [
            'idle','die'
        ]}

        self.load_sprites('idle', start_row=0, num_frames=8)
        self.load_sprites('die',start_row=13,num_frames=16)
        
        self.current_action = 'idle'
        self.index = 0
        self.image = self.sprites[self.current_action][self.index]
        self.flip = False
        self.rect = self.image.get_rect()
        self.rect.center = (1100, 150)
        self.frame_count = 0  # Contador de frames
        self.frame_delay = 9  # Número de updates para trocar o frame
    
   def load_sprites(self, action, start_row, num_frames):
        for i in range(num_frames):
            img = self.sprite_sheet.subsurface((288 * i, 128 * start_row), (288, 128))
            img = pygame.transform.scale(img, (288 * 6, 128 * 6))
            self.sprites[action].append(img)
    
   def change_action(self, action):
        if action != self.current_action:
            self.current_action = action
            self.index = 0

   def update(self):
        """
        Atualiza o frame da animação e aplica o flip na imagem se necessário.
        """
        self.frame_count += 1
        if self.frame_count >= self.frame_delay:
            self.frame_count = 0
            self.index = (self.index + 1) % len(self.sprites[self.current_action])
            self.image = self.sprites[self.current_action][self.index]
        
        # Aplica o flip na imagem se necessário
        if self.flip:
            self.image = pygame.transform.flip(self.sprites[self.current_action][self.index], True, False)
    
   def draw(self, surface):
        surface.blit(self.image, self.rect)

class Dayla(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        diretorio_DaylaClass = os.path.dirname(__file__)
        diretorio_assets = os.path.join(diretorio_DaylaClass, 'assets')
        diretorio_personagens = os.path.join(diretorio_assets, 'Personagens')
        diretorio_Dayla = os.path.join(diretorio_personagens, 'dayla')

        # Carregar o spritesheet
        self.sprite_sheet = pygame.image.load(os.path.join(diretorio_Dayla, 'EitanSpriteSheet.png')).convert_alpha()
        self.sprites = {action: [] for action in [
            'idle','die'
        ]}

        self.load_sprites('idle', start_row=0, num_frames=8)
        self.load_sprites('die',start_row=15,num_frames=12)
        
        self.current_action = 'idle'
        self.index = 0
        self.image = self.sprites[self.current_action][self.index]
        self.flip = False
        self.rect = self.image.get_rect()
        self.rect.center = (1000, 370)
        self.frame_count = 0  # Contador de frames
        self.frame_delay = 9  # Número de updates para trocar o frame
    
    def load_sprites(self, action, start_row, num_frames):
        for i in range(num_frames):
            img = self.sprite_sheet.subsurface((288 * i, 128 * start_row), (288, 128))
            img = pygame.transform.scale(img, (288 * 6, 128 * 6))
            self.sprites[action].append(img)
    
    def change_action(self, action):
        if action != self.current_action:
            self.current_action = action
            self.index = 0

    def update(self):
        """
        Atualiza o frame da animação e aplica o flip na imagem se necessário.
        """
        self.frame_count += 1
        if self.frame_count >= self.frame_delay:
            self.frame_count = 0
            self.index = (self.index + 1) % len(self.sprites[self.current_action])
            self.image = self.sprites[self.current_action][self.index]

        # Aplica o flip na imagem se necessário
        if self.flip:
            self.image = pygame.transform.flip(self.sprites[self.current_action][self.index], True, False)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

def drawWinnerScream(surface,p1,p2,winner,gameStage,estado):
    if p1 == 1:
        P1 = Wander()
    elif p1 == 2:
        P1 = Dayla()
    elif p1 == 3:
        P1 = Ayla()
    elif p1 == 4:
        P1 = Drax()
    
    if p2 == 1:
        P2 = Wander()
    elif p2 == 2:
        P2 = Dayla()
    elif p2 == 3:
        P2 = Ayla()
    elif p2 == 4:
        P2 = Drax()
    
    P2.flip = True
    P1.rect.center = (200,150)
    P2.rect.center = (1200, 150)
    start_time = pygame.time.get_ticks()
    font = pygame.font.SysFont("Arial", 72, bold=True)
    clock = pygame.time.Clock()
    fps = 120
    mouse = Mouse()
    running = True
    background = pygame.image.load("./assets/backWiner.jpg").convert()
    while running:
        current_time = pygame.time.get_ticks()  # Tempo atual
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.blit(background, (0, 0))
        
        # Atualizar e desenhar os personagens
        P1.update()
        P2.update()
        P1.draw(surface)
        P2.draw(surface)

        # Mostrar o texto de vitória após 3 segundos
        if current_time - start_time >= 3000:
            if winner == "p1":
                text_surface = font.render(f"PLAYER 1 WINS", True, (0, 0, 255))
                text_rect = text_surface.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))
                surface.blit(text_surface, text_rect)
                P2.change_action("die")
            elif winner == "p2":
                text_surface = font.render(f"PLAYER 2 WINS", True, (255, 0, 0))
                text_rect = text_surface.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))
                surface.blit(text_surface, text_rect)
                P1.change_action("die")
            elif winner == "draw":
                text_surface = font.render(f"DRAW", True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))
                surface.blit(text_surface, text_rect)

        # Verificar interações do mouse
        if mouse.is_over_area([1037, 658], [1338, 719]) and mouse.is_button_pressed(1):
            gameStage = 0
            estado = "menu"
            winner = ""
            return gameStage, estado, winner

        # Atualizar a tela
        pygame.display.flip()
        clock.tick(fps)

