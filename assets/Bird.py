import pygame

from assets.Obstacle import Obstacle

SPRITE_SWITCH_COUNT = 20


class Bird(Obstacle):

    def __init__(self, screen_object, resource_path_list, elevation):
        self.sprite_list = []
        for res in resource_path_list:
            self.sprite_list.append(pygame.image.load(res))
        self.sprite_list_length = len(self.sprite_list)
        self.active_sprite_index = 0
        self.counter = 0
        super().__init__(screen_object, resource_path_list[0], elevation)

    def move(self):
        if self.counter == SPRITE_SWITCH_COUNT:
            self.counter = 0
            self.active_sprite_index = self.active_sprite_index + 1 if self.active_sprite_index < self.sprite_list_length - 1 else 0
            self.sprite = self.sprite_list[self.active_sprite_index]
        super().move()
        self.counter += 1

    def show(self):
        super().show()

    def is_dead(self):
        return super().is_dead()

    def animate(self):
        self.move()
        self.show()