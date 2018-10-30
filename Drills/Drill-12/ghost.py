from pico2d import *
from math import *

import game_world
import random
import boy
import game_framework

Distance = 2 * 200 * 3.14
Second = 1
CMeter = 37.699104  #CMeter Per Second
Degree = 720
PixelPerCMeter = (1 / 0.03)
PixelPerSecond = (CMeter * PixelPerCMeter)
CMeterPerDegree = (CMeter / 720)
SecondPerDegree = (Second / Degree)

# PixelPerSecond = PixelPerMeter * Meter
# self.x = PixelPerSecond * game_framework.frame_time

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
        self.timer = 0
        self.opacity = random.uniform(0.0, 1.0)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x = self.x_standard + (100 * cos(self.rad))
        self.y = self.y_standard + (100 * sin(self.rad))
        if self.i < 100:
            self.image.opacify(self.opacity)
            self.i += 3
            t = self.i / 100
            self.x = (1 - t) * self.start_x + t * self.x
            self.y = (1 - t) * self.start_y + t * self.y
        else:
            self.rad += (4 * 3.141592) / 60
            self.timer += game_framework.frame_time
        if self.timer > 0.5:
            self.image.opacify(random.uniform(0.0, 1.0))
            self.timer = 0
