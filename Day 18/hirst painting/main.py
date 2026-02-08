from turtle import Turtle, Screen
import random
#import colorgram

# color = colorgram.extract('C:\\Users\\gdgeo\\PycharmProjects\\100 Days of Code - The Complete Python Pro Bootcamp\\python100\\Day 18\\hirst painting\\hello.jpg', 30)



colors_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

# for color in color:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print (rgb_colors)

screen = Screen()
screen.colormode(255)

# colors = ["coral", "cyan", "magenta", "yellow", "blue", "green", "orange", "purple"]
# angle= [90, 180, 270, 360]    

tim = Turtle()
tim.color("coral")
tim.pensize(20)

tim.penup()         
tim.goto(-255, -255)   
tim.pendown()


# for n in range(1000):
#     random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     random_angle = random.choice(angle)
#     tim.pencolor(random_color)
#     tim.forward(25)
#     tim.setheading(random_angle)
# # angle = 0
tim.penup()
for i in range(10):
    for j in range(10):
        random_color = random.choice(colors_list)
        tim.pencolor(random_color)
        tim.dot(20)
        
        tim.forward(50)
    tim.backward(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)

# # while angle < 360:
# #     random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# #     tim.pencolor(random_color)
# #     tim.setheading(angle)
# #     tim.circle(100)
# #     angle += 4






    



















screen.exitonclick()