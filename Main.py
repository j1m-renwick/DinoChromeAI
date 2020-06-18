import pygame
import numpy as np

from ObstacleGenerator import ObstacleGenerator
from assets.Dino import Dino
from assets.Ground import Ground
from Screen import Screen
from skynet.DinoBot import DinoBot
from skynet.Evolution import get_next_generation
from skynet.PredictiveNeuralNet import PredictiveNeuralNet

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (77, 75, 153)
LIGHT_BLUE = (233,245,249)

SCREEN_X = 1000
SCREEN_Y = 500
size = (SCREEN_X, SCREEN_Y)
GROUND_BASELINE = SCREEN_Y - 30
SCROLL_RATE = -7
screen_object = Screen(pygame.display.set_mode(size), GROUND_BASELINE, SCROLL_RATE)

pygame.init()

font = pygame.font.SysFont("helvetica mono", 28)

clock = pygame.time.Clock()
clock.tick(60)

# change this to enable one play-controlled dino for development
IS_PLAYER_CONTROLLED = False

# TODO make the elevation of birds random
obstacle_generator = ObstacleGenerator(screen_object, 60)
generation_counter = 1

ground = Ground(screen_object)

if IS_PLAYER_CONTROLLED:
    dino = Dino(screen_object)

obstacles = []

dino_population = []
dead_dinos = []

if not IS_PLAYER_CONTROLLED:
    for i in range(0, 50):
        dino_population.append(DinoBot(screen_object))

while True:

    for obst in obstacles:
        if obst.is_dead():
            obstacles.remove(obst)

    new_obstacle = obstacle_generator.generate()
    if new_obstacle is not None:
        obstacles.append(new_obstacle)

    screen_object.screen.fill(LIGHT_BLUE)

    ground.animate()

    for obst in obstacles:
        obst.animate()

    if IS_PLAYER_CONTROLLED:
        dino.animate()

    if not IS_PLAYER_CONTROLLED:
        for dino in dino_population:
            if screen_object.assess_death(dino, obstacles):
                dino_population.remove(dino)
                dead_dinos.append(dino)
            # the inputs to the bots
            yvel = dino.yvel / dino.VELOCITY_LIMIT
            next_obstacle = screen_object.get_next_obstacle(dino, obstacles)
            next_obstacle_dist = (next_obstacle.xpos - dino.xpos + dino.sprite_width) / SCREEN_X if next_obstacle is not None else 1
            next_obstacle_ypos = next_obstacle.ypos / GROUND_BASELINE if next_obstacle is not None else 1
            dino.input_data(np.array([yvel, next_obstacle_dist, next_obstacle_ypos]))
            dino.animate()

        if len(dino_population) == 0:
            generation_counter += 1
            dino_population = get_next_generation(dead_dinos, 0.1, screen_object)
            dead_dinos.clear()
            obstacles.clear()
            obstacle_generator.reset()

    label = font.render("GENERATION: " + str(generation_counter), 1, PURPLE)
    screen_object.screen.blit(label, (SCREEN_X - label.get_width() - 10, 10))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and IS_PLAYER_CONTROLLED:
                dino.jump()
            elif event.key == pygame.K_DOWN and IS_PLAYER_CONTROLLED:
                dino.duck()
            elif event.key == pygame.K_s:
                print('saving')
                dino_population[-1].net.persist('SavedBestBoy.bin')
            elif event.key == pygame.K_l:
                print('loading')
                generation_counter += 1
                dino_population.clear()
                for i in range(0, 50):
                    dino_population.append(DinoBot(screen_object, brain=PredictiveNeuralNet.load('SavedBestBoy.bin')))
                dead_dinos.clear()
                obstacles.clear()
                obstacle_generator.reset()