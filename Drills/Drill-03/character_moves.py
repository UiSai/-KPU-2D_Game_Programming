from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
s = 0
r = 200
rad = 0
deg = 270


def character_move_square():
    global x, y, s
    
    if (400 <= x < 400 + 380 and y == 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)
    elif (x == 400 + 380 and 90 <= y < 560):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.01)
    elif (20 < x <= 400 + 380 and y == 560):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.01)
    elif (x == 400 - 380 and 90 < y <= 560):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.01)
    elif (400 - 380 <= x < 400 and y == 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        s = s + 1
        delay(0.01)

def character_move_circle():
    global x, y, s, deg, rad, cp_x, cp_y


    rad = radians(deg)
    cp_x = 400 + (r * cos(rad))
    cp_y = 290 + (r * sin(rad))
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(cp_x, cp_y)
    deg = deg + 1
    if (cp_x <= 400 and 90 < cp_y <= 91):
        s = 0
        deg = 270
    delay(0.01)




while (True):
    if(s < 190):
        character_move_square()
    else:
        character_move_circle()
    
close_canvas()
