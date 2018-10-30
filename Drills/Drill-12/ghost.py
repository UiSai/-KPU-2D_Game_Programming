from pico2d import *
from math import *
import game_world

class Ghost:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ghost.image == None:
            Ghost.image = load_image('boy.png')
            
        self.x, self.y, self.velocity = x, y, velocity
        self.deg = 0
        self.rad = 0

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.deg += 1
        self.rad = radians(self.deg)
        self.x = 400 + (200 * cos(self.rad))
        self.y = 290 + (200 * sin(self.rad))
