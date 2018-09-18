from pico2d import *
from math import *

open_canvas()
hide_lattice()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')
frame = 0
point_count = 0
x_DB = (203, 132, 535, 477, 715, 316, 510, 692, 682, 712)
y_DB = (535, 243, 470, 203, 136, 225, 92, 518, 336, 349)


def move_point_to_point():
    global x_DB, y_DB, point_count
    x, y = x_DB[point_count], y_DB[point_count]  # 이동 중의 현재 좌표를 계산할 x, y값
    fix_x, fix_y = x_DB[point_count], y_DB[point_count]  # 기울기를 계산할 처음 위치의 고정 좌표값
    if (point_count == 9):  # 리스트(튜플) 반복 조건
        point_count = -1
    next_x, next_y = x_DB[point_count + 1], y_DB[point_count + 1]  # 목적지 좌표값

    i = (next_y - fix_y) / (next_x - fix_x)  # 기울기 계산. 기울기 값에 따라 속도가 달라짐. 함수 마지막 부분의 x 증가량으로 속도 조절.
    b = y - i * x  # 상수 계산

    while (abs(x - next_x) > 0 ):
        y = i * x + b  # 좌표값을 구함
        if (x - next_x < 0):
            run_to_right(x, y)
            x += 1
        else:
            run_to_left(x, y)
            x -= 1

    point_count += 1

def judge_value_plus_minus(fix_x, next_x, x):
    if (fix_x < next_x):
        x = x + 1
        return x
    else:
        x = x - 1
        return x

def run_to_right(x, y):
    global frame
    right = 100

    clear_canvas()
    character.clip_draw(frame * 100, right, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    get_events()

def run_to_left(x, y):
    global frame
    left = 0

    clear_canvas()
    character.clip_draw(frame * 100, left, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    get_events()

while True:
    move_point_to_point()

close_canvas()