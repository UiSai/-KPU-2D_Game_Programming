from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class mini_Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image('ball21x21.png')
        self.falling_speed = random.randint(5, 20)

    def update(self):
        if (self.y > 60):
            self.y -= self.falling_speed
        else:
            self.y = 60

    def draw(self):
        self.image.draw(self.x, self.y)

class big_Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image('ball41x41.png')
        self.falling_speed = random.randint(5, 20)

    def update(self):
        if (self.y > 60):
            self.y -= self.falling_speed
        else:
            self.y = 60

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()


mini_number = random.randint(1, 21)
print('작은 공의 개수 :', mini_number)
print('큰 공의 개수 :', 20 - mini_number)
team = [Boy() for i in range(11)]
balls = [mini_Ball() for i in range(mini_number)]
balls_2 = [big_Ball() for i in range(20 - mini_number)]
grass = Grass()

running = True

while running:
    handle_events()

    for boy in team:
        boy.update()
    for mini_ball in balls:
        mini_ball.update()
    for big_ball in balls_2:
        big_ball.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()
    for mini_ball in balls:
        mini_ball.draw()
    for big_ball in balls_2:
        big_ball.draw()

    update_canvas()
    delay(0.05)


close_canvas()