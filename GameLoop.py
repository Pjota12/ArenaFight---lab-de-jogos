import pygame
from pygame.locals import *
from draxClassP1 import DraxP1
from draxClassP2 import DraxP2
from aylaClassP1 import AylaP1
from aylaClassP2 import AylaP2
from daylaClassP1 import DaylaP1
from daylaClassP2 import DaylaP2
from wanderClassP1 import WanderP1
from wanderClassP2 import WanderP2
from cavernaClass import Caverna
from temploClass import Templo
from florestClass import Florest
from PPlay.keyboard import*
from PPlay.mouse import*
import os

pygame.font.init()

last_die = 0
def draw_health(surface, P1, P2):
    # Configurações das barras
    bar_width = 300  # Largura máxima da barra
    bar_height = 20  # Altura da barra
    spacing = 10     # Espaçamento entre as barras e do topo

    # Cores
    health_color = (255, 0, 0)  # Vermelho para vida
    background_color = (50, 50, 50)  # Cinza escuro para o fundo da barra

    # Barra de vida do P1
    p1_health_ratio = P1.life / P1.max_life
    pygame.draw.rect(surface, background_color, (150, spacing, bar_width, bar_height))
    pygame.draw.rect(surface, health_color, (150, spacing, bar_width * p1_health_ratio, bar_height))

    # Barra de vida do P2
    p2_health_ratio = P2.life / P2.max_life
    pygame.draw.rect(surface, background_color, (surface.get_width() - 150 - bar_width, spacing, bar_width, bar_height))
    pygame.draw.rect(surface, health_color, (surface.get_width() - 150 - bar_width, spacing, bar_width * p2_health_ratio, bar_height))


def draw_special(surface,P1,P2):
    # Configurações das barras
    bar_width = 300  # Largura máxima da barra
    bar_height = 20  # Altura da barra
    spacing = 10     # Espaçamento entre as barras e do topo

    special_color = (0, 0, 255)  # Azul para especial
    background_color = (50, 50, 50)  # Cinza escuro para o fundo da barra

    # Barra de especial do P1
    p1_special_ratio = P1.specialBar / P1.max_specialBar
    pygame.draw.rect(surface, background_color, (150, spacing + bar_height + 5, bar_width, bar_height))
    pygame.draw.rect(surface, special_color, (150, spacing + bar_height + 5, bar_width * p1_special_ratio, bar_height))

    # Barra de especial do P2
    p2_special_ratio = P2.specialBar / P2.max_specialBar
    pygame.draw.rect(surface, background_color, (surface.get_width() - 150 - bar_width, spacing + bar_height + 5, bar_width, bar_height))
    pygame.draw.rect(surface, special_color, (surface.get_width() - 150 - bar_width, spacing + bar_height + 5, bar_width * p2_special_ratio, bar_height))


def run_game_loop(surface,p1,p2,tempo,mapa,modo):
    global last_die
    diretorio_gameloop = os.path.dirname(__file__)
    diretorio_assets = os.path.join(diretorio_gameloop, 'assets')
    diretorio_personagens = os.path.join(diretorio_assets, 'Personagens')
    diretorio_wander = os.path.join(diretorio_personagens, 'wander')
    diretorio_dayla = os.path.join(diretorio_personagens, 'dayla')
    diretorio_ayla = os.path.join(diretorio_personagens, 'Ayla')
    diretorio_drax = os.path.join(diretorio_personagens, 'Drax')
    # Configuração do loop
    font = pygame.font.SysFont("Arial", 72, bold=True)
    clock = pygame.time.Clock()
    fps = 120
    round_atual = 1
    last_die = pygame.time.get_ticks() 
    check_if_sum = False


    all_sprites = pygame.sprite.Group()
    if p1 == 1:
        P1 = WanderP1()
        photoP1 = os.path.join(diretorio_wander, 'Wander.png')
    elif p1 == 2:
        P1 = DaylaP1()
        photoP1 = os.path.join(diretorio_dayla, 'Dayla.png')
    elif p1 == 3:
        P1 = AylaP1()
        photoP1 = os.path.join(diretorio_ayla, 'Ayla.png')
    elif p1 == 4:
        P1 = DraxP1()
        photoP1 = os.path.join(diretorio_drax, 'Drax.png')
    
    if p2 == 1:
        P2 = WanderP2()
        photoP2 = os.path.join(diretorio_wander, 'Wander.png')
    elif p2 == 2:
        P2 = DaylaP2()
        photoP2 = os.path.join(diretorio_dayla, 'Dayla.png')
    elif p2 == 3:
        P2 = AylaP2()
        photoP2 = os.path.join(diretorio_ayla, 'Ayla.png')
    elif p2  == 4:
        P2 = DraxP2()
        photoP2 = os.path.join(diretorio_drax, 'Drax.png')
    
    if mapa == 1:
        Mapa = Caverna()
    elif mapa == 2:
        Mapa = Templo()
    elif mapa == 3:
        Mapa = Florest()
    
    PhotoP1 = pygame.image.load(photoP1).convert_alpha()
    PhotoP2 = pygame.image.load(photoP2).convert_alpha()
    PhotoP1 = pygame.transform.scale(PhotoP1, (64 * 2, 64 * 2))
    PhotoP2 = pygame.transform.scale(PhotoP2, (64 * 2, 64 * 2))
    PhotoP2 = pygame.transform.flip(PhotoP2, True, False)
                                

    all_sprites.add(P1)
    all_sprites.add(P2)
    running = True

    winer = ''

    keybord = Keyboard()
    mouse = Mouse()



    if modo == 0:
        print("entrei no modo 0")
        start_time = pygame.time.get_ticks()  # Captura o tempo inicial
        total_time = tempo * 60 * 1000  # Converte o tempo de minutos para milissegundos
        P1.allowMoviment = True
        P2.allowMoviment = True
        while running:
            print(mouse.get_position())
            current_time = pygame.time.get_ticks()  # Tempo atual
            elapsed_time = current_time - start_time  # Tempo decorrido
            remaining_time = max(0, total_time - elapsed_time)  # Tempo restante

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Calcula minutos e segundos restantes
            minutes = remaining_time // 60000
            seconds = (remaining_time % 60000) // 1000



            # Exibe o timer no centro superior da tela
            timer_text = f"{minutes}:{seconds}"  # Formato MM:SS
            text_surface = font.render(timer_text, True, (255, 255, 255))  # Texto branco
            text_rect = text_surface.get_rect(center=(surface.get_width() // 2, 50))


            # print(mouse.get_position())

            # Captura as teclas pressionadas
            keys = pygame.key.get_pressed()

            # Desenha a caverna e obtém as plataformas
            plataformas = Mapa.draw(surface)

            # Atualiza o personagem com as plataformas
            P1.update(keys, plataformas, P2,modo)
            P2.update(keys, plataformas, P1,modo)

            if minutes == 0 and seconds == 0:
                if P1.kills > P2.kills:
                    winer = "p1"
                elif P1.kills < P2.kills:
                    winer = "p2"
                else:
                    winer = "draw"
                
                return 2,winer
                

            # Desenha o personagem
            draw_special(surface,P1,P2)
            surface.blit(PhotoP1,(20,20))
            surface.blit(PhotoP2,(surface.get_width() - 148, 20))
            surface.blit(text_surface, text_rect)
            if keybord.key_pressed("1"):
                P1.draw(surface)
                P2.draw(surface)
            else:
                all_sprites.draw(surface)

            
            # Atualiza a tela
            pygame.display.flip()

            if keybord.key_pressed("ESCAPE"):
                return 0,''

            clock.tick(fps)
    if modo == 1:
        print("entrei no modo 1")
        while running:
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                
            keys = pygame.key.get_pressed()

            # Desenha a caverna e obtém as plataformas
            plataformas = Mapa.draw(surface)

            # Atualiza o personagem com as plataformas
            P1.update(keys, plataformas, P2,modo)
            P2.update(keys, plataformas, P1,modo)

            
            if not P1.allowMoviment and not P2.allowMoviment:
                text_surface = font.render(f"Round {round_atual}", True, (255, 255, 255))  # Texto branco
                text_rect = text_surface.get_rect(center=(surface.get_width() // 2 - 10, surface.get_height() // 2))
                surface.blit(text_surface, text_rect)
                if current_time - last_die >= 3000:
                    P1.allowMoviment = True
                    P2.allowMoviment = True
                    check_if_sum = False
            
            if P1.die or P2.die:
                last_die = current_time
                if not check_if_sum:
                    round_atual += 1
                    check_if_sum = True
            
            if P1.rounds_won >= (tempo//2)+1:
                winer = "p1"
                return 2,winer
            elif P2.rounds_won >= (tempo//2)+1:
                winer = "p2"
                return 2,winer

            draw_health(surface, P1, P2)
            draw_special(surface,P1,P2)
            surface.blit(PhotoP1,(20,20))
            surface.blit(PhotoP2,(surface.get_width() - 148, 20))
            if keybord.key_pressed("1"):
                P1.draw(surface)
                P2.draw(surface)
            else:
                all_sprites.draw(surface) # Desenha o personagem
        

            # Atualiza a tela
            pygame.display.flip()

            if keybord.key_pressed("ESCAPE"):
                return 0,''

            clock.tick(fps)

