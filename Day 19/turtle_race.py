from turtle import Turtle, Screen
import random

screen= Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will make you rich? Enter a color: ")
print(user_bet)
colour = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positin = [-70, -40, -10, 20, 50, 80]
all_turtles = []


# tim= Turtle(shape="turtle")
# tim.penup()
# tim.goto(-230, -100)





for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colour[i])
    tim.penup()
    tim.goto(-230, y_positin[i])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!🎊🤑💸💰")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!😔🥲😭")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

   

screen.exitonclick()
