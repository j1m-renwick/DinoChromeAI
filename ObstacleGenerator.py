import random

from assets.Bird import Bird
from assets.Cactus import Cactus

GENERATION_INTERVAL = 95

SMALL_CACTUS_GAP_COEFFICIENT = 40
LARGE_CACTUS_GAP_COEFFICIENT = 45
BIRD_GAP_COEFFICIENT = 60

small_cactus_obstacles = ["resources/cacti/cactus_small_1.png",
                          "resources/cacti/cactus_small_2.png",
                          "resources/cacti/cactus_small_3.png",
                          "resources/cacti/cactus_small_4.png",
                          "resources/cacti/cactus_small_5.png",
                          "resources/cacti/cactus_small_6.png"]

large_cactus_obstacles = ["resources/cacti/cactus_large_1.png",
                          "resources/cacti/cactus_large_2.png",
                          "resources/cacti/cactus_large_3.png",
                          "resources/cacti/cactus_large_4.png",
                          "resources/cacti/cactus_large_group_1.png"]

flying_obstacles = [(["resources/birds/bird_1.png", "resources/birds/bird_2.png"])]


class ObstacleGenerator:

    def __init__(self, screen_object, max_elevation_height):
        self.screen_object = screen_object
        self.max_elevation_height = max_elevation_height
        self.counter = 0

    def generate(self):
        if random.randint(0, 100) > GENERATION_INTERVAL:
            if self.counter <= 0:
                self.counter = 0
                return self.get_next_obstacle()
        # TODO put this in a tick method instead
        self.counter += self.screen_object.scroll_rate
        return None

    def get_next_obstacle(self):
        rand = random.random()
        if rand <= 0.3:
            self.counter = abs(SMALL_CACTUS_GAP_COEFFICIENT * self.screen_object.scroll_rate)
            return Cactus(self.screen_object, random.choice(small_cactus_obstacles))
        elif 0.3 < rand <= 0.7:
            self.counter = abs(LARGE_CACTUS_GAP_COEFFICIENT * self.screen_object.scroll_rate)
            return Cactus(self.screen_object, random.choice(large_cactus_obstacles))
        else:
            self.counter = abs(BIRD_GAP_COEFFICIENT * self.screen_object.scroll_rate)
            return Bird(self.screen_object, random.choice(flying_obstacles), random.randint(0, self.max_elevation_height))

    def reset(self):
        self.counter = 0
