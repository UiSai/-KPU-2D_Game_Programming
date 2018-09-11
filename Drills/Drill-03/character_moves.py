from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
s = 0

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
    global x, y, s

    if (400 <= x < 400 + 380 and 90 <= y < 160):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        y = y + 1
        delay(0.01)
    elif (400 <= x < 400 + 380 and 150 <= y < 230):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        y = y + 2
        delay(0.01)
    elif (400 <= x < 400 + 380 and 210 <= y < 300):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 1
        y = y + 2
        delay(0.01)

 
    elif (400 < x <= 400 + 380 and 300 <= y < 370):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 1
        y = y + 2
        delay(0.01)
    elif (400 < x <= 400 + 380 and 370 <= y < 440):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        y = y + 2
        delay(0.01)
    elif (400 < x <= 400 + 380 and 440 <= y < 510):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        y = y + 1
        delay(0.01)

        
    elif (400 - 380 < x <= 400 and 440 < y <= 510):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        y = y - 1
        delay(0.01)
    elif (400 - 380 < x <= 400 and 370 < y <= 440):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        y = y - 2
        delay(0.01)
    elif (400 - 380 < x <= 400 and 300 < y <= 370):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 1
        y = y - 2
        delay(0.01)

        
    elif (400 - 380 < x <= 400 and 230 < y <= 300):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 1
        y = y - 2
        delay(0.01)
    elif (400 - 380 < x <= 400 and 160 < y <= 230):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        y = y - 2
        delay(0.01)
    elif (400 - 380 < x <= 400 and 90 < y <= 160):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        y = y - 1
        s = s + 1
        if (y == 90):
            s = 0
        delay(0.01)

while (x < 1000):
    if(s < 190):
        character_move_square()
    else:
        character_move_circle()
    
close_canvas()
