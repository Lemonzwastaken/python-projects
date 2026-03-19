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
timmy.pensize(15)
timmy.speed("fast")

directions = [90,180,270,360]
color_list = ["red", "blue", "green", "yellow","purple", "orange", "magenta", "cyan", "brown", "pink"]

for i in range(int(input("How many walks do you wish to generate: "))):
    
    timmy.forward(30)

    timmy.right(random.choice(directions))

    timmy.color(random_color())



screen.exitonclick()