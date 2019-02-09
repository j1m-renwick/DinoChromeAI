from abc import ABC

import pygame


class Obstacle(ABC):

    def __init__(self, screen_object, active_sprite, elevation = None):
        self.screen = screen_object.screen
        self.xpos = self.screen.get_width()
        self.scroll_rate = screen_object.scroll_rate
        self.sprite = pygame.image.load(active_sprite)
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()
        self.ypos = screen_object.baseline - self.sprite_height
        if elevation is not None:
            self.ypos -= elevation

    def move(self):
        self.xpos = self.xpos + self.scroll_rate

    def show(self):
        self.screen.blit(self.sprite, [self.xpos, self.ypos, self.sprite_width, self.sprite_height])

    def is_dead(self):
        return self.xpos + self.sprite_width < 0

    def animate(self):
        self.move()
        self.show()