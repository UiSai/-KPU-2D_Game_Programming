from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def move_point_to_point(p1, p2):
    for i in range(0, 100 + 1, 5):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]  #parametric representation
        # print('test')
        if p1[0] > p2[0]:
            run_to_left_animation(x, y)
        else:
            run_to_right_animation(x, y)

    #draw_point(p2) # 마지막 점을 위 반복문에서 찍지 않기 때문에 별도로 찍어줘야 함

def run_to_right_animation(x, y):
    global frame
    right = 100
    handle_events()

    #clear_canvas()
    kpu_ground.draw(KPU_WIDTH / 2, KPU_HEIGHT / 2)
    character.clip_draw(frame * 100, right, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)

def run_to_left_animation(x, y):
    global frame
    left = 0
    handle_events()

    #clear_canvas()
    kpu_ground.draw(KPU_WIDTH / 2, KPU_HEIGHT / 2)
    character.clip_draw(0,left, 100, 100, x, y)
    character.clip_draw(frame * 100, left, 100, 100, pos[0[0]], pos[0[1]])
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    get_events()

def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
            print('bbye')
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            print('bye')

def draw_big_point(p):
    pass
    """
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))
    """

def draw_curve_points(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):

   # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        run_to_left_animation(x, y)

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        run_to_left_animation(x, y)
    #draw_point(p4)

   # draw p3-p4
    for i in range(0, 100, 2):
        print('start')
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p2[0] + (3*t**3 - 5*t**2 + 2) * p3[0] + (-3*t**3 + 4*t**2 + t) * p4[0] + (t**3 - t**2)*p5[0])/2
        y = ((-t**3 + 2*t**2 - t)*p2[1] + (3*t**3 - 5*t**2 + 2) * p3[1] + (-3*t**3 + 4*t**2 + t) * p4[1] + (t**3 - t**2)*p5[1])/2
        run_to_left_animation(x, y)
    #draw_point(p1)

    # draw p4-p5
    for i in range(0, 100, 2):
        print('start')
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p3[0] + (3*t**3 - 5*t**2 + 2) * p4[0] + (-3*t**3 + 4*t**2 + t) * p5[0] + (t**3 - t**2)*p6[0])/2
        y = ((-t**3 + 2*t**2 - t)*p3[1] + (3*t**3 - 5*t**2 + 2) * p4[1] + (-3*t**3 + 4*t**2 + t) * p5[1] + (t**3 - t**2)*p6[1])/2
        run_to_left_animation(x, y)
    #draw_point(p1)

    # draw p5-p6
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p4[0] + (3*t**3 - 5*t**2 + 2) * p5[0] + (-3*t**3 + 4*t**2 + t) * p6[0] + (t**3 - t**2)*p7[0])/2
        y = ((-t**3 + 2*t**2 - t)*p4[1] + (3*t**3 - 5*t**2 + 2) * p5[1] + (-3*t**3 + 4*t**2 + t) * p6[1] + (t**3 - t**2)*p7[1])/2
        run_to_left_animation(x, y)
    #draw_point(p1)

    # draw p6-p7
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p5[0] + (3*t**3 - 5*t**2 + 2) * p6[0] + (-3*t**3 + 4*t**2 + t) * p7[0] + (t**3 - t**2)*p8[0])/2
        y = ((-t**3 + 2*t**2 - t)*p5[1] + (3*t**3 - 5*t**2 + 2) * p6[1] + (-3*t**3 + 4*t**2 + t) * p7[1] + (t**3 - t**2)*p8[1])/2
        run_to_left_animation(x, y)
    #draw_point(p1)

    # draw p7-p8
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p6[0] + (3*t**3 - 5*t**2 + 2) * p7[0] + (-3*t**3 + 4*t**2 + t) * p8[0] + (t**3 - t**2)*p9[0])/2
        y = ((-t**3 + 2*t**2 - t)*p6[1] + (3*t**3 - 5*t**2 + 2) * p7[1] + (-3*t**3 + 4*t**2 + t) * p8[1] + (t**3 - t**2)*p9[1])/2
        run_to_left_animation(x, y)
    #draw_point(p1)

    # draw p8-p9
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p7[0] + (3*t**3 - 5*t**2 + 2) * p8[0] + (-3*t**3 + 4*t**2 + t) * p9[0] + (t**3 - t**2)*p10[0])/2
        y = ((-t**3 + 2*t**2 - t)*p7[1] + (3*t**3 - 5*t**2 + 2) * p8[1] + (-3*t**3 + 4*t**2 + t) * p9[1] + (t**3 - t**2)*p10[1])/2
        run_to_left_animation(x, y)
    #draw_point(p1)

    # draw p9-p10
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p8[0] + (3*t**3 - 5*t**2 + 2) * p9[0] + (-3*t**3 + 4*t**2 + t) * p10[0] + (t**3 - t**2)*p1[0])/2
        y = ((-t**3 + 2*t**2 - t)*p8[1] + (3*t**3 - 5*t**2 + 2) * p9[1] + (-3*t**3 + 4*t**2 + t) * p10[1] + (t**3 - t**2)*p1[1])/2
        run_to_left_animation(x, y)
    #draw_point(p1)

    # draw p10-p1
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p9[0] + (3*t**3 - 5*t**2 + 2) * p10[0] + (-3*t**3 + 4*t**2 + t) * p1[0] + (t**3 - t**2)*p2[0])/2
        y = ((-t**3 + 2*t**2 - t)*p9[1] + (3*t**3 - 5*t**2 + 2) * p10[1] + (-3*t**3 + 4*t**2 + t) * p1[1] + (t**3 - t**2)*p2[1])/2
        run_to_left_animation(x, y)
    #draw_point(p1)





size = 10
pos = [(random.randint(0, 800), random.randint(0, 600)) for i in range(size)] #list comprehension
n = 1

open_canvas(KPU_WIDTH, KPU_HEIGHT)
hide_lattice()
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')
frame = 0
running = True

while running:
    draw_curve_points(pos[0], pos[1], pos[2], pos[3], pos[4], pos[5], pos[6], pos[7], pos[8], pos[9])
    #n = (n + 1) % size