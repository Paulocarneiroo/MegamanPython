import pygame as pg
from settings import *
from sys import exit
from Sprite import *

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Megaman')
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.sprite = Sprite(self, x_position=10, y_position=10, x_velocity=10, y_velocity=10)

    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        self.sprite.draw()

    def update(self):
        self.sprite.animate()
        self.clock.tick(FPS)
        pg.display.flip()


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.QUIT
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key in self.sprite.key_state:
                    self.sprite.key_state[event.key] = True
                    self.sprite.control()
            elif event.type == pg.KEYUP:
                if event.key in self.sprite.key_state:
                    self.sprite.key_state[event.key] = False
                    self.sprite.control()
                    self.sprite.x_direction = 0
                    self.sprite.y_direction = 0

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
