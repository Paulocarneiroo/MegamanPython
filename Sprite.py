from settings import *
import pygame as pg


class Sprite:
    def __init__(self, game, x_position, y_position, x_velocity, y_velocity):
        self.game = game
        self.position = dict(x=x_position, y=y_position)
        self.velocity = dict(x=x_velocity, y=y_velocity)
        self.color = MEGAMAN_COLOR
        self.width = WIDTH
        self.height = HEIGHT
        self.gravity = GRAVITY
        self.key_state = {pg.K_RIGHT: False, pg.K_LEFT: False, pg.K_UP: False}
        self.x_direction = 0
        self.y_direction = 0
        self.jump_velocity = -18
        self.image = pg.image.load('megaman.png').convert_alpha()

    def draw_megaman(self):
        self.game.screen.blit(self.image, (self.position['x'], self.position['y']))
        #pg.draw.rect(self.game.screen,
                 #    self.color,
                  #   (self.position['x'],
                   #   self.position['y'],
                   #   self.width, self.height), 25)

    def draw(self):
        self.draw_megaman()

    def animate(self):
        self.draw()

        # atualiza a velocidade vertical do retângulo (incluindo ação da gravidade)
        self.velocity['y'] += self.gravity
        self.velocity['y'] = min(self.velocity['y'], 30)

        # atualiza posição do retângulo na vertical
        self.position['y'] += self.velocity['y']

        if self.position['y'] + self.height >= FIELD_H:
            self.velocity['y'] = 0
            self.gravity = 0
        else:
            self.gravity = GRAVITY

        self.position['x'] += self.x_direction * self.velocity['x']
        if self.position['x'] < 0:
            self.position['x'] = 0

    def control(self):
        if self.key_state[pg.K_RIGHT]:
            self.x_direction = 1
        elif self.key_state[pg.K_LEFT]:
            self.x_direction = -1
        else:
            self.x_direction = 0

        if self.key_state[pg.K_UP] and self.position['y'] + self.height >= FIELD_H:
            # inicia pulo (seta velocidade vertical para valor negativo)
            self.velocity['y'] = self.jump_velocity
            self.y_direction = 1
        else:
            self.y_direction = 0


