from pico2d import *
import random
"""
def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))
"""

def move_point_to_point(p1, p2):
    for i in range(0, 100 + 1, 5):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        run_to_left_animation(x, y)

    #draw_point(p2) # 마지막 점을 위 반복문에서 찍지 않기 때문에 별도로 찍어줘야 함

"""
def move_line(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    for i in range(0, 100 + 1, 5):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        draw_point((x, y))

    draw_point(p2) # 마지막 점을 위 반복문에서 찍지 않기 때문에 별도로 찍어줘야 함
"""
def run_to_right_animation(x, y):
    global frame
    right = 100

    clear_canvas()
    grass.draw(400, 0)
    character.clip_draw(frame * 100, right, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    get_events()

def run_to_left_animation(x, y):
    global frame
    left = 0

    clear_canvas()
    grass.draw(400, 0)
    character.clip_draw(frame * 100, left, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    get_events()

size = 10
position = [(random.randint(0, 800), random.randint(0, 600)) for i in range(size)]
n = 1


open_canvas()
hide_lattice()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
frame = 0
point_count = 0

while True:
    move_point_to_point(position[n - 1], position[n])
    n = (n + 1) % size
