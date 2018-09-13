from pico2d import *
open_canvas()
grass = load_image('grass.png')
"""
character = load_image('run_animation.png')

x = 0
frame = 0
while(x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)
    get_events()

close_canvas()
"""
character = load_image('animation_sheet.png')

x = 0
frame = 0

def run_to_right():
    global x, frame

    right = 100
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, right, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x += 7
    delay(0.05)
    get_events()

def run_to_left():
    global x, frame

    left = 0
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, left, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x -= 7
    delay(0.05)
    get_events()

while(x < 900):
    run_to_right()
    if(x > 790):
        while(x > 10):
            run_to_left()
close_canvas()