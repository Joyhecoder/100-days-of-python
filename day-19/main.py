from turtle import Turtle, Screen

#! class notes
# tim = Turtle()
# screen = Screen()


# def move_forwards():
#     tim.forward(10)

# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()


# ? challenge 1
# ? w = forwards / s = backwards / a = counter-clockwise / d = clockwise / c = clear drawing
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(15)


def move_backwards():
    tim.backward(15)


def turn_right():
    tim.right(45)
    tim.forward(15)
    
def turn_left():
    tim.left(45)
    tim.forward(15)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
