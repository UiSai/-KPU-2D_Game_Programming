from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_first_coordinates_to_second():
    x, y = 203, 535  # 이동 중의 현재 좌표를 계산할 x, y값
    fix_x, fix_y = 203, 535  # 기울기를 계산할 처음 위치의 고정 좌표값
    next_x, next_y = 132, 243  # 목적지 좌표값

    i = (next_y - y) / (next_x - x)  # 기울기 계산
    b = fix_y - i * fix_x  # 상수 계산

    while (abs(x - next_x) > 0 ):
        y = i * x + b  # 좌표값을 구함

        clear_canvas_now()  # 캔버스 삭제
        character.draw_now(x, y)  # 캔버스에 그림
        x -= 1
        delay(0.01)

def move_second_coordinates_to_third():
    x, y = 132, 243
    fix_x, fix_y = 132, 243
    next_x, next_y = 535, 470

    i = (next_y - y) / (next_x - x)
    b = fix_y - i * fix_x

    while (abs(x - next_x) > 0 ):
        y = i * x + b

        clear_canvas_now()
        character.draw_now(x, y)
        x += 1
        delay(0.01)

def move_third_coordinates_to_fourth():
    x, y = 535, 470
    fix_x, fix_y = 535, 470
    next_x, next_y = 477, 203

    i = (next_y - y) / (next_x - x)
    b = fix_y - i * fix_x

    while (abs(x - next_x) > 0 ):
        y = i * x + b

        clear_canvas_now()
        character.draw_now(x, y)
        x -= 1
        delay(0.01)

def move_fourth_coordinates_to_fifth():
    x, y = 477, 203
    fix_x, fix_y = 477, 203
    next_x, next_y = 715, 136

    i = (next_y - y) / (next_x - x)
    b = fix_y - i * fix_x

    while (abs(x - next_x) > 0 ):
        y = i * x + b

        clear_canvas_now()
        character.draw_now(x, y)
        x += 1
        delay(0.01)

def move_fifth_coordinates_to_sixth():
    x, y = 715, 136
    fix_x, fix_y = 715, 136
    next_x, next_y = 316, 225

    i = (next_y - y) / (next_x - x)
    b = fix_y - i * fix_x

    while (abs(x - next_x) > 0 ):
        y = i * x + b

        clear_canvas_now()
        character.draw_now(x, y)
        x -= 1
        delay(0.01)

def move_sixth_coordinates_to_seventh():
    x, y = 316, 225
    fix_x, fix_y = 316, 225
    next_x, next_y = 510, 92

    i = (next_y - y) / (next_x - x)
    b = fix_y - i * fix_x

    while (abs(x - next_x) > 0 ):
        y = i * x + b

        clear_canvas_now()
        character.draw_now(x, y)
        x += 1
        delay(0.01)

def move_seventh_coordinates_to_eighth():
    x, y = 510, 92
    fix_x, fix_y = 510, 92
    next_x, next_y = 692, 518

    i = (next_y - y) / (next_x - x)
    b = fix_y - i * fix_x

    while (abs(x - next_x) > 0 ):
        y = i * x + b

        clear_canvas_now()
        character.draw_now(x, y)
        x += 1
        delay(0.01)

def move_eighth_coordinates_to_ninth():
    x, y = 692, 518
    fix_x, fix_y = 692, 518
    next_x, next_y = 682, 336

    i = (next_y - y) / (next_x - x)
    b = fix_y - i * fix_x

    while (abs(x - next_x) > 0 ):
        y = i * x + b

        clear_canvas_now()
        character.draw_now(x, y)
        x -= 1
        delay(0.01)

def move_ninth_coordinates_to_tenth():
    x, y = 682, 336
    fix_x, fix_y = 682, 336
    next_x, next_y = 712, 349

    i = (next_y - y) / (next_x - x)
    b = fix_y - i * fix_x

    while (abs(x - next_x) > 0 ):
        y = i * x + b

        clear_canvas_now()
        character.draw_now(x, y)
        x += 1
        delay(0.01)

def move_tenth_coordinates_to_first():
    x, y = 712, 349
    fix_x, fix_y = 712, 349
    next_x, next_y = 203, 535

    i = (next_y - y) / (next_x - x)
    b = fix_y - i * fix_x

    while (abs(x - next_x) > 0 ):
        y = i * x + b

        clear_canvas_now()
        character.draw_now(x, y)
        x -= 1
        delay(0.01)


while True:
    move_first_coordinates_to_second()
    move_second_coordinates_to_third()
    move_third_coordinates_to_fourth()
    move_fourth_coordinates_to_fifth()
    move_fifth_coordinates_to_sixth()
    move_sixth_coordinates_to_seventh()
    move_seventh_coordinates_to_eighth()
    move_eighth_coordinates_to_ninth()
    move_ninth_coordinates_to_tenth()
    move_tenth_coordinates_to_first()

close_canvas()
