import pygame

IMAGE_OFFSET = 20


class Ground:

    def __init__(self, screen_object):
        self.sprite = pygame.image.load("resources/ground_large_short.png")
        self.screen = screen_object.screen
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()
        self.xpos = 0
        self.ypos = screen_object.baseline - IMAGE_OFFSET
        self.scroll_rate = screen_object.scroll_rate

    def move(self):
        self.xpos = self.xpos + self.scroll_rate if self.xpos + self.sprite_width > 0 else self.scroll_rate

    def show(self):
        self.screen.blit(self.sprite, [self.xpos, self.ypos, self.sprite_width, self.sprite_height])
        self.screen.blit(self.sprite, [self.xpos + self.sprite_width, self.ypos, self.sprite_width, self.sprite_height])

    def animate(self):
        self.move()
        self.show()
