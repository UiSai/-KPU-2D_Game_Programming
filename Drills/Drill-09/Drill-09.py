from pico2d import *
import random

# Game object class here
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

# initialization code
open_canvas()

#boy = Boy()
team = [Boy() for i in range(11)]
balls = [mini_Ball() for i in range(11)]
balls_2 = [big_Ball() for j in range(11)]
grass = Grass()



running = True


# game main loop code
while running:
    handle_events()

    #team.update()
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()
    for ball in balls_2:
        ball.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    for ball in balls_2:
        ball.draw()

    update_canvas()

    delay(0.05)


# finalization code
close_canvas()