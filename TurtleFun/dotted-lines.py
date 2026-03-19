import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()

timmy.shape('turtle')
timmy.color('LimeGreen')
timmy.pensize(2)

#Draws dotted lines
def draw_dotted_line(paces = int(input("How many cycles do you want timmy to go through: "))):    
    for move in range(paces):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

draw_dotted_line()


screen.exitonclick()