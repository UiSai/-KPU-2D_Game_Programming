from pico2d import *
from math import *

import game_world
import random
import boy

class Ghost:
    image = None

    def __init__(self, start_x, start_y):
        if Ghost.image == None:
            Ghost.image = load_image('boy.png')
        self.x, self.y = 0, 0
        self.x_standard, self.y_standard = random.randint(50, 1550), random.randint(50, 550)
        self.deg = 0
        self.rad = 0
        self.i = 0
        self.start_x = start_x
        self.start_y = start_y

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.deg += 1
        self.rad = radians(self.deg)
        self.x = self.x_standard + (100 * cos(self.rad))
        self.y = self.y_standard + (100 * sin(self.rad))
        self.image.opacify(random.uniform(0.0, 1.0))
        if self.i < 100:
            self.i += 3
            t = self.i / 100
            self.x = (1 - t) * self.start_x + t * self.x
            self.y = (1 - t) * self.start_y + t * self.y