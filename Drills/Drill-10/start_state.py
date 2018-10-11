import game_framework
from pico2d import *
import start_state


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('kpu_credit.png')


def exit():
    global image
    del(image)


def update():
    pass


def draw():
    pass




def handle_events():
    events = get_events()

    pass


def pause(): pass


def resume(): pass


open_canvas()
game_framework.run(start_state)
close_canvas()