from turtle import Turtle, Screen
import random

Screen = Screen()
Screen.setup(width=500, height=400)
user_bet = Screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_start = -130
turtles = []
race_on = False

for colour in colors:
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(colour)
    tim.goto(x=-230, y=y_start)
    y_start += 50

    turtles.append(tim)


print(turtles)

if user_bet:
    race_on = True



while race_on:

    for turtle in turtles:
        turtle.forward(random.randint(0,10))

        if turtle.xcor() >= 230.0:
            race_on = False
            if turtle.pencolor() == user_bet:
                print("YOU WIN!!!")
            else:
                print("YOU LOOSE")
            
            break







Screen.exitonclick()