import turtle

import colorgram
from turtle import Turtle, Screen
import random


# colors = colorgram.extract('hirst.jpg', 20)
# # print(colors)
#
#
# for color in colors:
#     rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
#     color_list.append(rgb)

color_list = [(201, 167, 134), (236, 243, 249), (144, 51, 99), (163, 167, 41), (238, 71, 125), (237, 83, 61), (17, 140, 64), (241, 221, 67), (225, 118, 163), (10, 142, 179), (67, 198, 219), (157, 59, 53), (23, 169, 129), (32, 187, 202), (127, 188, 163), (107, 42, 88), (248, 231, 0)]

tom = Turtle()
new_screen = Screen()
turtle.colormode(255)
starting_pos = (-250, -250)
tom.speed("fastest")
tom.penup()
tom.goto(starting_pos)
tom.hideturtle()


def turtle_paint(color):
    tom.dot(20, color)


def turtle_move_right():
    tom.goto(int(tom.pos()[0])+50, int(tom.pos()[1]))


def turtle_move_up():
    tom.goto(int(starting_pos[0]), int(tom.pos()[1]) + 50)


for i in range(10):
    for q in range(10):
        random_color = random.choice(color_list)
        turtle_paint(random_color)
        turtle_move_right()
    turtle_move_up()



new_screen.exitonclick()



