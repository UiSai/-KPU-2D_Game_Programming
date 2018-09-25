from pico2d import *
from math import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

point_count = 0
frame = 100

"""
def calculate_position():  #move_point_to_point
    global character_x, character_y, goto_x, goto_y  # point_count는 리스트 내의 좌표를 가리킨다.
    #x, y = goto_x, goto_y  # 기울기를 계산할 처음 위치의 좌표값. 이동 중에는 x, y값이 현재 좌표로 바뀜.

    if (goto_x != character_x):
        i = ((goto_y - character_y) / (goto_x - character_x))  # 기울기 계산. 기울기 값에 따라 속도가 달라짐. 함수 마지막 부분의 x 증가량으로 속도 조절.
        b = character_y - (i * character_x)  # 일차함수의 상수 계산
        if (character_x < goto_x):
            while (goto_x - character_x > 0):
                character_y = i * character_x + b  # 좌표값을 구함
                return 'right'
                #draw_screen('right', character_x, character_y)
                # run_to_right_animation(character_x, character_y)
                #character_x += 10  # 이 값이 커질 수록 애니메이션을 더 넓게 찍음
        elif (goto_x < character_x):
            while (goto_x - character_x < 0):
                character_y = i * character_x + b
                return 'left'
                #draw_screen('left', character_x, character_y)
                # run_to_left_animation(character_x, character_y)
                #character_x -= 10
    else:
        draw_screen('stand', character_x, character_y)
"""

def draw_base():  # 배경이나 커서처럼 기본으로 찍어줘야 할 그림들
    global cursor_x, cursor_y
    # clear_canvas와 update_canvas는 외부에서 해줘야 함
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw(cursor_x, cursor_y)
    # 배경 찍고 커서 찍어야함. 순서 바뀌면 배경에 묻힘. 다른거 추가할 때도 참조.


def judge_direction():  # 이동 방향을 판단해줌.
    global character_x, character_y, goto_x, goto_y  # point_count는 리스트 내의 좌표를 가리킨다.
    #x, y = goto_x, goto_y  # 기울기를 계산할 처음 위치의 좌표값. 이동 중에는 x, y값이 현재 좌표로 바뀜.
    if (character_x < goto_x):
            return 'right'
            #draw_screen('right', character_x, character_y)
            # run_to_right_animation(character_x, character_y)
            #character_x += 10  # 이 값이 커질 수록 애니메이션을 더 넓게 찍음
    elif (goto_x < character_x):
            return 'left'
            #draw_screen('left', character_x, character_y)
            # run_to_left_animation(character_x, character_y)
            #character_x -= 10
    else:
        return 'stand'

def move_calculation():  #직선의 방정식 계산
    global character_x, character_y, goto_x, goto_y

    if (goto_x != character_x):
        i = ((goto_y - character_y) / (goto_x - character_x))  # 기울기 계산. 기울기 값에 따라 속도가 달라짐. 함수 마지막 부분의 x 증가량으로 속도 조절.
        #print(character_y)
        b = character_y - (i * character_x)  # 일차함수의 상수 계산
        #print(character_y)
        return i, b
    else:
        return 0, 0 #정지 상태를 위해 0, 0 반환을 넣음.



def draw_moving_screen():
    global frame, goto_x, goto_y, character_x, character_y
    direction = judge_direction()
    left = 0
    right = 100

    #handle_events()
    print(direction)
    i, b = move_calculation()
    character_y = i * character_x + b  # 캐릭터 좌표값을 구함
    #calculate_position(goto_x, goto_y)
    if direction == 'right':
        while (goto_x - character_x > 0):
            clear_canvas()
            draw_base()
            character_y = i * character_x + b
            character.clip_draw(frame * 100, right, 100, 100, character_x, character_y)
            frame = (frame + 1) % 8
            character_x += 5
            delay(0.05)
            handle_events()
            update_canvas()
    elif direction == 'left':
        while (goto_x - character_x < 0):
            clear_canvas()
            draw_base()
            character_y = i * character_x + b
            character.clip_draw(frame * 100, left, 100, 100, character_x, character_y)
            frame = (frame + 1) % 8
            character_x -= 5
            delay(0.05)
            handle_events()
            update_canvas()
    else:
        clear_canvas()
        draw_base()
        character.clip_draw(100, right, 100, 100, character_x, character_y)
        handle_events()
        update_canvas()

""" 이전 버전
def draw_moving_screen(direction, draw_x, draw_y):  #direction으로 방향 표기(문자열), draw_x/y로 캐릭터 표시 좌표 표기
    global frame, cursor_x, cursor_y, goto_x, goto_y, character_x, character_y
    left = 0
    right = 100

    handle_events()
    update_canvas()
    #calculate_position(goto_x, goto_y)
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if (direction == 'right'):
        cursor.draw(cursor_x, cursor_y)
        character.clip_draw(frame * 100, right, 100, 100, draw_x, draw_y)
        handle_events()
        #move_point_to_point(goto_x, goto_y)
    elif (direction == 'left'):
        cursor.draw(cursor_x, cursor_y)
        character.clip_draw(frame * 100, left, 100, 100, draw_x, draw_y)
    elif (direction == 'stand'):
        cursor.draw(cursor_x, cursor_y)
        character.clip_draw(100, 0, 100, 100, draw_x, draw_y)
        
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
"""

""" 
def run_to_right_animation(x, y):
    global frame
    right = 100

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    get_events()

def run_to_left_animation(x, y):
    global frame
    left = 0

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, left, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    get_events()
"""

def handle_events():
    global running
    global cursor_x, cursor_y
    global goto_x, goto_y

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            cursor_x, cursor_y = event.x, KPU_HEIGHT - 1 - event.y  #커서 조정
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                goto_x, goto_y = event.x, KPU_HEIGHT - 1 - event.y  #캐릭터의 목적지
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image("hand_arrow.png")

running = True
cursor_x, cursor_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
character_x, character_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
goto_x, goto_y = character_x, character_y
frame = 0
hide_cursor()

while running:
    #character.clip_draw(frame * 100, 100 * 1, 100, 100, goto_x - 25, goto_y + 26)
    #move_point_to_point(goto_x, goto_y)
    draw_moving_screen()