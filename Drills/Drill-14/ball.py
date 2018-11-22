from pico2d import *
import main_state
import game_world
import random


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, main_state.background.w), random.randint(0, main_state.background.h)

    def get_bb(self):
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        return cx - 10, cy - 10, cx + 10, cy + 10

    def set_background(self, bg):
        self.bg = bg

    def draw(self):
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.draw(cx, cy)

    def update(self):
        pass

    def stop(self):
        pass
