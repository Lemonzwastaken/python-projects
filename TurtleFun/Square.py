import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()

timmy.shape('turtle')
timmy.color('LimeGreen')
timmy.pensize(2)


#Draws a square
def draw_square(size = int(input("What size do you want the square to be: "))):  
    for move in range(4):
        timmy.forward(size)
        timmy.right(90)
        
draw_square()

screen.exitonclick()