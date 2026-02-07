from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

colors = ["coral", "cyan", "magenta", "yellow", "blue", "green", "orange", "purple"]
angle= [90, 180, 270, 360]    

tim = Turtle()
tim.color("coral")
tim.pensize(1)
tim.speed("fastest")

for n in range(1000):
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    random_angle = random.choice(angle)
    tim.pencolor(random_color)
    tim.forward(25)
    tim.setheading(random_angle)
# angle = 0
# while angle < 360:
#     random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     tim.pencolor(random_color)
#     tim.setheading(angle)
#     tim.circle(100)
#     angle += 4






    



















screen.exitonclick()