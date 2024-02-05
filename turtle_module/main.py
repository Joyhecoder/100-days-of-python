#? ------------- turtle square ----------------
# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("pink")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)




#? ------------- import modules with aliases ----------------
import turtle as t
from turtle import Screen

tim = t.Turtle()

#? ------------- draw dashed line ----------------
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()



#? ------------- draw different shapes ----------------
import random
colors= ['yellow', 'red', 'blue', 'green']
def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)  
    
screen = Screen()
screen.exitonclick()