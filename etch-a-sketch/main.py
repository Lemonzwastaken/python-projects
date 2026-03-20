import turtle as t

timmy = t.Turtle()
screen = t.Screen()

screen.listen()

#functions
def move_forwards():
    timmy.forward(10)

def turn_left():
    timmy.left(5)

def turn_right():
    timmy.right(5)

def clear_screen():
    screen.clearscreen()

def pen_up():
    timmy.penup()

def pen_down():
    timmy.pendown()

def change_thickness():
    size = timmy.pensize()
    size += 1
    timmy.pensize(size)

def reduce_thickness():
    size = timmy.pensize()
    if size <= 1:
        pass
    else:
        size -= 1
    timmy.pensize(size)


#RUNNING

screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear_screen)
screen.onkey(key="z", fun=pen_up)
screen.onkey(key="x", fun=pen_down)
screen.onkey(key="q", fun=change_thickness)
screen.onkey(key="e", fun=reduce_thickness)












screen.exitonclick()