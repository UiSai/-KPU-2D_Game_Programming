from pico2d import *
from math import *

import game_world
import random

class Ghost:
    image = None

    def __init__(self):
        if Ghost.image == None:
            Ghost.image = load_image('boy.png')
        self.x, self.y = 0, 0
        self.x_standard, self.y_standard = random.randint(50, 1550), random.randint(50, 750)
        self.deg = 0
        self.rad = 0

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.deg += 1
        self.rad = radians(self.deg)
        self.x = self.x_standard + (200 * cos(self.rad))
        self.y = self.y_standard + (200 * sin(self.rad))
        self.image.opacify(0.5)
