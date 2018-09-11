import turtle
import random

turtle.shape("turtle")

circle_x, circle_y, circle_range = 0, 0, 0
circle_range_LD_x, circle_range_LD_y = 0, 0
circle_range_RU_x, circle_range_RU_y = 0, 0
turtle_x, turtle_y = 0, 0

def random_circle():
    global circle_x, circle_y, circle_range

    circle_x, circle_y = random.randint(-500, 500), random.randint(-500, 500)
    circle_range = random.randint(50, 150)
    
    turtle.penup()
    turtle.goto(circle_x, circle_y - circle_range)
    turtle.pendown()
    turtle.circle(circle_range)
    turtle.penup()
    turtle.goto(0, 0)

def move_up():
    global turtle_x, turtle_y
    
    turtle.setheading(90)
    turtle.forward(50.0)
    turtle_x, turtle_y = turtle.position()
    print(turtle_x, turtle_y)
    Check()
    

def move_down():
    global turtle_x, turtle_y
    
    turtle.setheading(270)
    turtle.forward(50)
    turtle_x, turtle_y = turtle.position()
    print(turtle_x, turtle_y)
    Check()
    
def move_left():
    global turtle_x, turtle_y
    
    turtle.setheading(180)
    turtle.forward(50)
    turtle_x, turtle_y = turtle.position()
    print(turtle_x, turtle_y)
    Check()

def move_right():
    global turtle_x, turtle_y
    
    turtle.setheading(0)
    turtle.forward(50)
    turtle_x, turtle_y = turtle.position()
    print(turtle_x, turtle_y)
    Check()

def set_GameOver_Line():
    global circle_x, circle_y, circle_range
    global circle_range_LD_x, circle_range_LD_y
    global circle_range_RU_x, circle_range_RU_y

    circle_range_LD_x, circle_range_LD_y = circle_x - circle_range, circle_y - circle_range 
    circle_range_RU_x, circle_range_RU_y = circle_x + circle_range, circle_y + circle_range

    print(circle_range_LD_x, circle_range_LD_y)
    print(circle_range_RU_x, circle_range_RU_y)

def Check():
    global turtle_x, turtle_y
    global circle_range_LD_x, circle_range_LD_y, circle_range_RU_x, circle_range_RU_x
    
    if (circle_range_LD_x <= turtle_x <= circle_range_RU_x and circle_range_LD_y  <= turtle_y <= circle_range_RU_y):
        print(turtle_x, turtle_y)
        GameOver()

    
def GameOver():
    turtle.write("Game Over. Press Esc to reset.")

def reset():
    turtle.reset()

    global circle_x, circle_y, circle_range
    global circle_range_LD_x, circle_range_LD_y
    global circle_range_RU_x, circle_range_RU_y
    
    circle_x, circle_y, circle_range = 0, 0, 0
    circle_range_LD_x, circle_range_LD_y = 0, 0
    circle_range_RU_x, circle_range_RU_y = 0, 0
    turtle_x, turtle_y = 0, 0

    random_circle()
    set_GameOver_Line()


random_circle()
set_GameOver_Line()

turtle.onkey(move_up, 'Up')
turtle.onkey(move_down, 'Down')
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(reset, 'Escape')
turtle.listen()


