from pico2d import *
from ball import Ball

import game_world

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE, LSHIFT_DOWN, RSHIFT_DOWN, LSHIFT_UP, RSHIFT_UP, DASH_TIMER = range(11)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_LSHIFT): LSHIFT_DOWN,
    (SDL_KEYDOWN, SDLK_RSHIFT): RSHIFT_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): LSHIFT_UP,
    (SDL_KEYUP, SDLK_RSHIFT): RSHIFT_UP
}


# Boy States
class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity = 1
        elif event == LEFT_DOWN:
            boy.velocity = -1
        elif event == RIGHT_UP:
            boy.velocity = 0
        elif event == LEFT_UP:
            boy.velocity = 0
        boy.timer = 1000
        boy.velocity = 0

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dir >= 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity = 1
        elif event == LEFT_DOWN:
            boy.velocity = -1
        elif event == RIGHT_UP:
            boy.velocity = -1
        elif event == LEFT_UP:
            boy.velocity = 1
        elif event == LSHIFT_DOWN:
            if boy.velocity > 0:
                boy.velocity = 2
            else:
                boy.velocity = -2
        elif event == LSHIFT_UP:
            if boy.velocity > 0:
                boy.velocity = 1
            else:
                boy.velocity = -1
        elif event == RSHIFT_DOWN:
            if boy.velocity > 0:
                boy.velocity = 1
            else:
                boy.velocity = -1
        elif event == RSHIFT_UP:
            if boy.velocity > 0:
                boy.velocity = 1
            else:
                boy.velocity = -1
        boy.dir = boy.velocity

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if boy.velocity > 0:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:

    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100,
                                          3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100,
                                          -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)


class DashState:

    @staticmethod
    def enter(boy, event):
        if event == LSHIFT_DOWN:
            if boy.velocity > 0:
                boy.velocity = 3
            else:
                boy.velocity = -2
        elif event == LSHIFT_UP:
            if boy.velocity > 0:
                boy.velocity = 1
            else:
                boy.velocity = -1
        elif event == RSHIFT_DOWN:
            if boy.velocity > 0:
                boy.velocity = 3
            else:
                boy.velocity = -3
        elif event == RSHIFT_UP:
            if boy.velocity > 0:
                boy.velocity = 1
            else:
                boy.velocity = -1
        boy.frame = 0
        boy.dir = boy.velocity
        boy.dash_timer = 300

    @staticmethod
    def exit(boy, event):
        if boy.velocity > 0:
            boy.velocity = 1
        else:
            boy.velocity = -1

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 1600 - 75)
        boy.dash_timer -= 1
        if boy.dash_timer == 0:
            boy.add_event(DASH_TIMER)

    @staticmethod
    def draw(boy):
        if boy.velocity > 0:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SLEEP_TIMER: SleepState, SPACE: IdleState, LSHIFT_DOWN: IdleState, RSHIFT_DOWN: IdleState,
                LSHIFT_UP: IdleState, RSHIFT_UP: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState,
               LSHIFT_DOWN: DashState, RSHIFT_DOWN: DashState, LSHIFT_UP: RunState, RSHIFT_UP: RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState},
    DashState: {LSHIFT_DOWN: IdleState, RSHIFT_DOWN: IdleState, LSHIFT_UP: RunState, RSHIFT_UP: RunState,
                RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
                DASH_TIMER: RunState, SPACE: DashState}
}


class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity


class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def fire_ball(self):
        print('FIRE BALL')
        ball = Ball(self.x, self.y, self.dir * 3)
        game_world.add_object(ball, 1)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
