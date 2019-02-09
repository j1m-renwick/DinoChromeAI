import pygame

SPRITE_SWITCH_COUNT = 15
GRAVITY = 1
JUMP_VEL = -19


class Dino:
    yvel = 0
    is_jumping = False
    is_ducking = False
    VELOCITY_LIMIT = 15

    def __init__(self, screen_object):
        self.running_sprite_list = []
        self.running_sprite_list.append(pygame.image.load("resources/dino/dino_large_running_1.png"))
        self.running_sprite_list.append(pygame.image.load("resources/dino/dino_large_running_2.png"))
        self.ducking_sprite_list = []
        self.ducking_sprite_list.append(pygame.image.load("resources/dino/dino_large_ducking_1.png"))
        self.ducking_sprite_list.append(pygame.image.load("resources/dino/dino_large_ducking_2.png"))
        self.active_sprite_list = self.running_sprite_list
        self.sprite = self.active_sprite_list[0]
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()
        self.screen = screen_object.screen
        self.xpos = 50
        self.screen_object = screen_object
        self.baseline_ypos = screen_object.baseline - self.sprite_height
        self.ypos = self.baseline_ypos
        self.sprite_switch_counter = 0
        self.duck_counter = 0
        self.active_sprite_index = 0

    def move(self):
        if self.sprite_switch_counter == SPRITE_SWITCH_COUNT:
            self.sprite_switch_counter = 0
            self.active_sprite_index = 1 if self.active_sprite_index == 0 else 0
            self.sprite = self.active_sprite_list[self.active_sprite_index]
        self.update_velocity()
        self.update_ducking()
        self.sprite_switch_counter += 1

    def show(self):
        self.screen.blit(self.sprite, [self.xpos, self.ypos, self.sprite_width, self.sprite_height])

    def animate(self):
        self.move()
        self.show()

    def update_velocity(self):
        if self.is_jumping:
            self.yvel = min(self.yvel + GRAVITY, self.VELOCITY_LIMIT)
            self.ypos += self.yvel
            self.ypos = min(self.ypos, self.baseline_ypos)
            if self.ypos == self.baseline_ypos:
                self.is_jumping = False

    def update_ducking(self):
        if self.is_ducking:
            self.duck_counter -= 1
            if self.duck_counter == 0:
                self.switch_sprite_data(False)

    def jump(self):
        if not self.is_jumping and not self.is_ducking:
            self.yvel = JUMP_VEL
            self.is_jumping = True

    def duck(self):
        if not self.is_jumping:
            self.duck_counter = 30
            self.switch_sprite_data(True)

    def switch_sprite_data(self, is_ducking):
        self.is_ducking = is_ducking
        self.active_sprite_list = self.ducking_sprite_list if is_ducking else self.running_sprite_list
        self.sprite = self.ducking_sprite_list[0] if is_ducking else self.running_sprite_list[0]
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()
        self.ypos = self.screen_object.baseline - self.sprite_height
        self.sprite_switch_counter = 0
        self.active_sprite_index = 0

