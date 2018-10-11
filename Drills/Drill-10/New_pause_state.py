import game_framework
from pico2d import *

import main_state

name = "PauseState"
image = None
pause_second = 0.0


def enter():
    global image
    global pause_second
    image = load_image('pause.png')
    pause_second = 0


def exit():
    global image
    del(image)


def update():
    pass


def draw():
    global image
    global pause_second

    if (pause_second < 0.5):
        clear_canvas()
        main_state.draw()
        image.draw(400, 300)
        update_canvas()
        delay(0.01)
        pause_second += 0.01
    elif (0.5 < pause_second < 1):
        clear_canvas()
        main_state.draw()
        update_canvas()
        delay(0.01)
        pause_second += 0.01
    else:
        pause_second = 0


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.pop_state()


def pause(): pass


def resume(): pass