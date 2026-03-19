import turtle
import random

timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)

timmy.color('LimeGreen')
timmy.speed(0)

radius = int(input("What is the radius of the circle: "))
increment = int(input("How much space do you want between the circles: "))

for rad in range(int(360/increment)):

    timmy.circle(radius)
    timmy.right(increment)
    timmy.color(random_color())


screen.exitonclick()