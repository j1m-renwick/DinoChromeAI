import pygame


class Screen:

    def __init__(self, screen, baseline, scroll_rate):
        self.screen = screen
        self.baseline = baseline
        self.scroll_rate = scroll_rate

    def assess_death(self, dino, obstacles):
        dino_mask = pygame.mask.from_surface(dino.sprite)

        for obstacle in obstacles:
            obstacle_mask = pygame.mask.from_surface(obstacle.sprite)
            if not (dino_mask.overlap(obstacle_mask,
                                          (int(obstacle.xpos - dino.xpos), int(obstacle.ypos - dino.ypos))) is None):
                return True
        return False

    def get_next_obstacle(self, dino, obstacles):
        best_obstacle = None
        # TODO refactor to remove this hardcoding
        best_dist = 10000
        for obstacle in obstacles:
            dist = obstacle.xpos - dino.xpos + dino.sprite_width
            if 0 < dist < best_dist:
                best_dist = dist
                best_obstacle = obstacle
        return best_obstacle
