from assets.Obstacle import Obstacle


class Cactus(Obstacle):

    def __init__(self, screen_object, resource_path):
        super().__init__(screen_object, resource_path)

    def move(self):
        super().move()

    def show(self):
        super().show()

    def is_dead(self):
        return super().is_dead()

    def animate(self):
        self.move()
        self.show()
