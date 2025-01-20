import pygame
from pygame.locals import*
import os


class DaylaP1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        diretorio_EitanClass = os.path.dirname(__file__)
        diretorio_assets = os.path.join(diretorio_EitanClass, 'assets')
        diretorio_personagens = os.path.join(diretorio_assets, 'Personagens')
        diretorio_Eitan = os.path.join(diretorio_personagens, 'dayla')

        # Carregar o spritesheet
        self.sprite_sheet = pygame.image.load(os.path.join(diretorio_Eitan, 'DaylaSpriteSheet.png')).convert_alpha()

        # Inicializar as animações
        self.sprites = {action: [] for action in [
            'idle', 'walk',  'attack1', 'attack2', 'attack3',
            'super_attack', 'block', 'roll', 'air_attack', 'hit' ,'up','down','die'
        ]}

        self.load_sprites('idle', start_row=0, num_frames=8)
        self.load_sprites('walk', start_row=1, num_frames=8)
        self.load_sprites('attack1', start_row=9, num_frames=6)
        self.load_sprites('attack2', start_row=10, num_frames=8)
        self.load_sprites('attack3', start_row=11, num_frames=18)
        self.load_sprites('super_attack', start_row=12, num_frames=10)
        self.load_sprites('block', start_row=13, num_frames=12)
        self.load_sprites('roll', start_row=6, num_frames=7)
        self.load_sprites('air_attack', start_row=5, num_frames=8)
        self.load_sprites('hit', start_row=14, num_frames=6)
        self.load_sprites('up',start_row=2,num_frames=3)
        self.load_sprites('down',start_row=3,num_frames=3)
        self.load_sprites('die',start_row=15,num_frames=12)


        #__Configurações iniciais__
        self.current_action = 'idle'
        self.index = 0
        self.image = self.sprites[self.current_action][self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (300, 370)
        self.current_time = 0

        #___Movimento e estado___
        self.flip = False
        self.is_jumping = False
        self.is_blocking = False
        self.is_hit = False
        self.on_ground = True
        self.velocity_y = 0
        self.gravity = 0.6
        self.speed = 5.5  # Velocidade do movimento
        self.cooldown_timer = 0  # Frames de invulnerabilidade
        self.roll_distance = 10  # Distância percorrida na rolagem
        self.die = False
        self.die_moment = 0
        self.allowMoviment = False


        #___HIT BOX___
        #atack hitBOX config
        self.attack_rect = pygame.Rect(0, 0, 0, 0)
        #atack hitBOX config
        self.personagem_rect = pygame.Rect(
                self.rect.x + 227,
                self.rect.y + 174,
                60,
                90
            )
        
        #__BLOQUEIO CONFIG__
        self.is_blocking = False
        self.last_block_time = 0
        self.cooldown_timer_block = 0

        #___ATAQUES CONFIGS___
        #cooldown ataques config
        self.is_attacking = {
            'attack1':False,
            'attack2':False,
            'attack3':False
        }
        self.cooldown_timer_attacks = {
            'attack1':0,
            'attack2':0,
            'attack3':0,
        }
        self.last_attack_time = {
            'attack1':0,
            'attack2':0,
            'attack3':0,
        }
        self.attacks_duration = {
            'attack1':12,
            'attack2':18,
            'attack3':41,
        }
        #special configs
        self.specialBar = 0
        self.max_specialBar = 100
        self.is_doing_special = False
        self.cooldown_timer_special = 0
        

        #___KNOCKBACK___
        #knockback configs
        self.knockback_multiplier = 2 # Inicialmente sem knockback
        self.knockback_speed = 2  # Velocidade base do empurrão
        self.knockback_velocity = [0, 0]  # [x_velocity, y_velocity]
        self.knockbak_force = 0

        #__X1MODE CONFIG__
        self.life = 200
        self.max_life = 200
        self.rounds_won = 0
        self.demage = 0

        #__CLASSIC MODE__
        self.kills = 0
        self.addknockback = 0


    def load_sprites(self, action, start_row, num_frames):
        for i in range(num_frames):
            img = self.sprite_sheet.subsurface((288 * i, 128 * start_row), (288, 128))
            img = pygame.transform.scale(img, (288 * 2, 128 * 2))
            self.sprites[action].append(img)

    def change_action(self, action):
        if action != self.current_action:
            self.current_action = action
            self.index = 0

    def jump(self):
        if not self.is_jumping and self.on_ground:
            self.is_jumping = True
            self.velocity_y = -15
            self.on_ground = False

    def take_hit(self, atacker,modo):
        print(f'atacante flip {atacker.flip}, selfflip {self.flip} ')
        if self.is_blocking and atacker.flip != self.flip:
            print("ataque foi bloqueado")
        else:
            print(f"{atacker.current_action} causou um impacto no oponente!")
            self.is_hit = True
            self.cooldown_timer = 15  # Frames de invulnerabilidade

            # Define o multiplicador de knockback de forma estática para cada golpe
            self.knockback_multiplier = atacker.knockbak_force / 10

            # Calcula o vetor de força do knockback
            direction = -1 if atacker.flip else 1  # Define a direção com base no flip
            self.knockback_velocity = [
            direction * self.knockback_speed * self.knockback_multiplier,  # Horizontal
            -self.knockback_speed * self.knockback_multiplier / 2  # Vertical
            ]

            if modo == 0:
                self.knockback_speed += atacker.addknockback
            if modo == 1:
                self.life -= atacker.demage
            if atacker.specialBar <= 100:
                atacker.specialBar += 2.5

        

    def check_collision(self, other,modo):
        if self.attack_rect.colliderect(other.personagem_rect):
            if not other.is_hit:  # Garantir que o oponente não está em cooldown
                other.take_hit(self,modo)


    def handle_actions(self, keys):
        if self.allowMoviment:
            if not self.on_ground:  # Verifica se está no ar
                if keys[pygame.K_c] or keys[pygame.K_v] or keys[pygame.K_f]:
                    self.change_action('air_attack')
                    self.addknockback = 0.2
                    self.knockbak_force = 3
                    self.demage = 5
                    return  # Evita que outras ações sobreponham o ataque aéreo

                if self.velocity_y < 0:
                    self.change_action('up')
                elif self.velocity_y > 0:
                    self.change_action('down')

                if keys[pygame.K_a]:
                    self.flip = True
                    self.rect.x -= self.speed * 2
                if keys[pygame.K_d]:
                    self.flip = False
                    self.rect.x += self.speed * 2
                
                if self.die:
                    self.change_action('die')
            else:
                if keys[pygame.K_c] and self.cooldown_timer_attacks['attack1'] >= 0:
                    self.knockbak_force = 2
                    self.demage = 5
                    self.addknockback = 0.2
                    self.change_action('attack1')
                    self.is_attacking['attack1'] = True
                elif keys[pygame.K_v] and self.cooldown_timer_attacks['attack2'] >= 0:
                    self.knockbak_force = 5
                    self.demage = 7.5
                    self.addknockback = 0.5
                    self.change_action('attack2')
                    self.is_attacking['attack2'] = True
                elif keys[pygame.K_f] and self.cooldown_timer_attacks['attack3'] >= 0:
                    self.knockbak_force = 10
                    self.demage = 10
                    self.addknockback = 0.6
                    self.change_action('attack3')
                    self.is_attacking['attack3'] = True
                elif keys[pygame.K_g] and self.specialBar >= 100:
                    self.change_action('super_attack')
                    self.knockbak_force = 500
                    self.demage = 100
                    self.addknockback - 0.6
                    if not self.is_doing_special:
                        self.cooldown_timer_special = 25
                    self.is_doing_special = True
                elif keys[pygame.K_b] and self.cooldown_timer_block >= 0:
                    self.change_action('block')
                    self.is_blocking = True
                elif keys[pygame.K_s]:
                    self.change_action('roll')
                    if self.flip:
                        self.rect.x -= self.roll_distance  # Rola para a esquerda
                    else:
                        self.rect.x += self.roll_distance  # Rola para a direita
                elif keys[pygame.K_d]:
                    self.rect.x += self.speed
                    self.flip = False
                    if self.on_ground:
                        self.change_action('walk')
                elif keys[pygame.K_a]:
                    self.rect.x -= self.speed
                    self.flip = True
                    if self.on_ground:
                        self.change_action('walk')
                elif keys[pygame.K_w]:
                    self.jump()
                elif self.is_hit:
                    self.change_action('hit')
                elif self.die:
                    self.change_action('die')
                else:
                    if self.velocity_y < 0 and not self.is_hit:
                        self.change_action('up')
                    elif self.velocity_y > 0 and not self.is_hit:
                        self.change_action('down')
                    else:
                        if not self.is_hit:
                            self.change_action('idle')

    def update(self, keys, plataformas, other,modo):
        # Atualiza a colisão com o oponente
        self.check_collision(other,modo)

        self.current_time = pygame.time.get_ticks()

        # print(self.current_time)

        # Atualizar animação
        center = self.rect.center  # Manter o centro do retângulo

        #manter quadrado de hitbox no personagem
        if self.flip:
            self.personagem_rect = pygame.Rect(
                self.rect.x + 265,
                self.rect.y + 170,
                50,
                90
            )
        else:
            self.personagem_rect = pygame.Rect(
                self.rect.x + 260,
                self.rect.y + 170,
                50,
                90
            )

        self.index += 0.25
        if self.index >= len(self.sprites[self.current_action]):
            self.index = 0
        self.image = self.sprites[self.current_action][int(self.index)]
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(center=center)

        if self.is_hit:
        # Aplica o knockback
            self.rect.x += self.knockback_velocity[0]
            self.rect.y += self.knockback_velocity[1]

            # Amortecimento exponencial para o knockback
            damping_factor = 0.8  # Quanto menor, mais rápido o knockback para (0 < damping_factor < 1)
            gravity_force = self.gravity * 0.5  # Ajusta a gravidade durante o knockback

            self.knockback_velocity[0] *= damping_factor
            self.knockback_velocity[1] += gravity_force

            self.cooldown_timer -= 1

            # Finaliza o knockback 
            if  self.cooldown_timer <= 0:
                self.knockback_velocity = [0, 0]
                self.is_hit = False
                self.change_action('idle')

        if not self.die:
            self.haddle_is_die(modo,other)

        if self.die and modo == 0:
            if self.current_time - self.die_moment >= 3000:
                other.kills += 1
                self.rect.center = (300, 370)
                self.knockback_speed = 2
                self.die = False
        
        if self.die and modo == 1:
            if self.current_time - self.die_moment >= 2500:
                other.rounds_won += 1
                self.restart()
                other.restart() 


        
        #ATAQUER CONTROLADOR
        if self.is_doing_special:
            self.cooldown_timer_special -= 1
            if self.cooldown_timer_special <= 0:
                self.specialBar = 0
                self.is_doing_special = False
                self.change_action('idle')
        
        if not self.is_attacking['attack1'] and keys[pygame.K_c] and (self.current_time - self.last_attack_time['attack1'] >= 1300):
            self.cooldown_timer_attacks['attack1'] = self.attacks_duration['attack1']
            self.last_attack_time['attack1'] = self.current_time
        
        if not self.is_attacking['attack2'] and keys[pygame.K_v] and (self.current_time - self.last_attack_time['attack2'] >= 3500):
            self.cooldown_timer_attacks['attack2'] = self.attacks_duration['attack2']
            self.last_attack_time['attack2'] = self.current_time
        
        if not self.is_attacking['attack3'] and keys[pygame.K_f] and (self.current_time - self.last_attack_time['attack3'] >= 4500):
            self.cooldown_timer_attacks['attack3'] = self.attacks_duration['attack3']
            self.last_attack_time['attack3'] = self.current_time
        
        if not self.is_blocking and keys[pygame.K_b] and (self.current_time - self.last_block_time >= 5000):
            self.cooldown_timer_block = 23
            self.last_block_time = self.current_time

        

        # Verificar plataformas
        self.on_ground = False
        for plataforma in plataformas:
            if (
                self.rect.bottom <= plataforma.top + 20
                and self.rect.bottom + self.velocity_y >= plataforma.top
                and self.rect.centerx >= plataforma.left
                and self.rect.centerx <= plataforma.right
            ):
                self.rect.bottom = plataforma.top
                self.on_ground = True
                self.is_jumping = False
                self.velocity_y = 0

                if self.is_hit:
                    self.knockback_velocity[1] = 0
                break
        
        
        # Aplicar gravidade
        if not self.on_ground:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y
            if  keys[pygame.K_c] or keys[pygame.K_v] or keys[pygame.K_f]:
                self.addknockback = 0.2
                self.knockbak_force = 3
                self.demage = 5
                self.change_action('air_attack')

        else:
            self.velocity_y = 0
        

        # Movimentação e ações
        self.handle_actions(keys)

        if self.is_attacking['attack1']:
            self.cooldown_timer_attacks['attack1'] -=1
            if self.cooldown_timer_attacks['attack1'] <= 0:
                self.cooldown_timer_attacks['attack1'] = 0
                self.is_attacking['attack1'] = False
                self.change_action('idle')
        
        if self.is_attacking['attack2']:
            self.cooldown_timer_attacks['attack2'] -=1
            if self.cooldown_timer_attacks['attack2'] <= 0:
                self.cooldown_timer_attacks['attack2'] = 0
                self.is_attacking['attack2'] = False
                self.change_action('idle')

        if self.is_attacking['attack3']:
            self.cooldown_timer_attacks['attack3'] -=1
            if self.cooldown_timer_attacks['attack3'] <= 0:
                self.cooldown_timer_attacks['attack3'] = 0
                self.is_attacking['attack3'] = False
                self.change_action('idle')
        
        if self.is_blocking:
            self.cooldown_timer_block -= 1
            if self.cooldown_timer_block <= 0:
                self.is_blocking = False
                self.change_action('idle')
        
        # Atualizando o retângulo de colisão
        self.update_attack_rect()

    def update_attack_rect(self):
        if self.current_action == 'attack1':
            if self.flip:
                if 1 <= self.index < 5:
                    self.attack_rect = pygame.Rect(self.rect.x + 192, self.rect.y + self.rect.height - 65, 85, 30)  # Retângulo de ataque 1
                else:
                    self.attack_rect = pygame.Rect(0, 0, 0, 0)  # Ataque inativo
            else:
                if 1 <= self.index < 7:
                    self.attack_rect = pygame.Rect(self.rect.x + 300, self.rect.y + self.rect.height - 65, 85, 30)  # Retângulo de ataque 1
                else:
                    self.attack_rect = pygame.Rect(0, 0, 0, 0)  # Ataque inativo
        elif self.current_action == 'attack2':
            if self.flip:
                if 1 <= self.index < 4:
                    self.attack_rect = pygame.Rect(self.rect.x + 192, self.rect.y + self.rect.height - 65, 85, 30)
                elif 5 <= self.index < 8:
                    self.attack_rect = pygame.Rect(self.rect.x + 185, self.rect.y + self.rect.height - 70, 95, 55)
                else:
                    self.attack_rect = pygame.Rect(0, 0, 0, 0)  # Ataque inativo
            else:
                if 1 <= self.index < 4:
                    self.attack_rect = pygame.Rect(self.rect.x + 300, self.rect.y + self.rect.height - 65, 85, 30)  
                elif 5 <= self.index < 8:
                    self.attack_rect = pygame.Rect(self.rect.x + 290, self.rect.y + self.rect.height - 70, 95, 55)
                else:
                    self.attack_rect = pygame.Rect(0, 0, 0, 0)  # Ataque inativo
        elif self.current_action == 'attack3':
            if self.flip:
                if 0 <= self.index < 3:
                    self.attack_rect = pygame.Rect(self.rect.x + 192, self.rect.y + self.rect.height - 65, 85, 30)
                elif 3 <= self.index < 6:
                    self.attack_rect = pygame.Rect(self.rect.x + 185, self.rect.y + self.rect.height - 70, 95, 55)
                elif 8<= self.index < 17:
                    self.attack_rect = pygame.Rect(self.rect.x + 175, self.rect.y + self.rect.height - 110, 100, 100)
                else:
                    self.attack_rect = pygame.Rect(0, 0, 0, 0)  # Ataque inativo # Ataque inativo
            else:
                if 0 <= self.index < 3:
                    self.attack_rect = pygame.Rect(self.rect.x + 300, self.rect.y + self.rect.height - 65, 85, 30) 
                elif 3 <= self.index < 6:
                    self.attack_rect = pygame.Rect(self.rect.x + 290, self.rect.y + self.rect.height - 70, 95, 55)
                elif 8<= self.index < 17:
                    self.attack_rect = pygame.Rect(self.rect.x + 300, self.rect.y + self.rect.height - 110, 100, 100)
                else:
                    self.attack_rect = pygame.Rect(0, 0, 0, 0)  
        elif self.current_action == 'air_attack':
            if self.flip:
                if 2 <= self.index < 8:
                    self.attack_rect = pygame.Rect( self.rect.x + 150, self.rect.y + 155, 120, 50) # Air ataque
                else:
                    self.attack_rect = pygame.Rect(0, 0, 0, 0)  # Ataque inativo
            else:
                if 2 <= self.index < 8:
                    self.attack_rect = pygame.Rect(self.rect.x + 305 , self.rect.y + 155, 120, 50)  # Air ataque
                else:
                    self.attack_rect = pygame.Rect(0, 0, 0, 0)  # Ataque inativo
        elif self.current_action == 'super_attack':
            if self.flip:
                if 2 <= self.index <4:
                    self.attack_rect = pygame.Rect(self.rect.x + 180, self.rect.y + self.rect.height - 70, 200, 75)  # Super ataque
                elif 4 <= self.index < 10:
                    self.attack_rect = pygame.Rect(self.rect.x + 75, self.rect.y + self.rect.height - 100, 375, 100)  # Super ataque
                elif 10<= self.index < 11:
                    self.attack_rect = pygame.Rect(self.rect.x + 180, self.rect.y + self.rect.height - 70, 200, 75)  # Super ataque
                else:
                    self.attack_rect = pygame.Rect(0, 0, 0, 0)  # Ataque inativo
            else:
                if 2 <= self.index <4:
                    self.attack_rect = pygame.Rect(self.rect.x + 180, self.rect.y + self.rect.height - 70, 200, 75)  # Super ataque
                elif 4 <= self.index < 10:
                    self.attack_rect = pygame.Rect(self.rect.x + 125, self.rect.y + self.rect.height - 100, 375, 100)  # Super ataque
                elif 10<= self.index < 11:
                    self.attack_rect = pygame.Rect(self.rect.x + 180, self.rect.y + self.rect.height - 70, 200, 75)  # Super ataque
                else:
                    self.attack_rect = pygame.Rect(0, 0, 0, 0)  # Ataque inativo
        else:
            self.attack_rect = pygame.Rect(0, 0, 0, 0)  # Nenhuma colisão ativa

    def haddle_is_die(self,modo,other):
        if modo == 0 and self.personagem_rect.x < -100 or self.personagem_rect.x > 1500 or self.personagem_rect.y > 750:
            self.die = True
            self.die_moment = self.current_time
        elif modo == 1 and self.personagem_rect.x < -100 or self.personagem_rect.x > 1500 or self.personagem_rect.y > 750 or self.life <= 0:
            self.die = True
            self.die_moment = self.current_time
    def restart(self):
        self.rect.center = (300, 370)
        self.die = False
        self.allowMoviment = False
        self.life = 200
        self.knockback_speed = 2
        self.flip = False
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        pygame.draw.rect(surface, (255, 0, 0), self.personagem_rect, 2)  # Retângulo do personagem
        pygame.draw.rect(surface, (0, 255, 0), self.attack_rect, 2)  # Retângulo de ataque