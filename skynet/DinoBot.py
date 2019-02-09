from assets.Dino import Dino
from skynet.PredictiveNeuralNet import PredictiveNeuralNet
import numpy as np


class DinoBot(Dino):
    score = 0

    def __init__(self, screen_object, brain=None):
        super().__init__(screen_object)
        if brain is not None:
            self.net = brain
        else:
            # Distance to next object; vertical speed
            self.net = PredictiveNeuralNet([3, 10, 3])
        self.fitness = -1

    def input_data(self, data):
        self.net.setInputData(data)

    def move(self):
        if not self.is_ducking and not self.is_jumping:
            self.score += 1.2
        else:
            self.score += 1
        data = self.net.predict()
        # if data[0][0] < 0.5:
        #     super().jump()
        # else:
        #     super().duck()
        index = np.argmax(data)
        if index == 0:
            super().jump()
        elif index == 1:
            super().duck()
        super().move()

    def show(self):
        super().show()

    def animate(self):
        self.move()
        self.show()
