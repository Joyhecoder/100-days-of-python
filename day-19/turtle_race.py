from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False

#set up the screen size
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which tutle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtules = []

def create_a_turtle(color, y_value):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y = y_value)
    all_turtules.append(new_turtle)
    

y = -150
for item in colors:
    create_a_turtle(item, y_value=y)
    y += 60
    
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtules:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You guessed right! {winning_color} turtle is the winner!")
            else:
                print(f"Sorry, you missed! {winning_color} turtle is the winner.")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
    
    
    
screen.listen()
screen.exitonclick()