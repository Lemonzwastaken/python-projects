import turtle
import random

timmy = turtle.Turtle()
screen = turtle.Screen()

timmy.shape('turtle')
timmy.color('LimeGreen')
timmy.pensize(2)

#Draws multiple side shapes from a single point with different colors

color_list = ["red", "blue", "green", "yellow","purple", "orange", "magenta", "cyan", "brown", "pink"]

def draw_multi_shape(sides = int(input("Max shape size: "))):

    for side in range(3,sides):
        angle = 360/side
        timmy.color(random.choice(color_list))
        for sider in range(side):
            timmy.forward(100)
            timmy.right(angle)



draw_multi_shape()


screen.exitonclick()