import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# for i in range(3, 10):
#     angle = float(360/i)
#     R = random.random()
#     G = random.random()
#     B = random.random()
#     tim.pencolor((R, G, B))
#     for t in range(i):
#         tim.forward(100)
#         tim.right(angle)


def turn_right():
    tim.right(90)
    tim.forward(20)


def turn_left():
    tim.left(90)
    tim.forward(20)


def turn_around():
    tim.right(180)
    tim.forward(20)

walk = True
movement = ["left", "right", "forward", "around"]
tim.pensize(1)
tim.speed(0)
turtle.colormode(255)

# while walk:
#     choice = random.choice(movement)
#     R = random.random()
#     G = random.random()
#     B = random.random()
#     tim.pencolor((R, G, B))
#     if choice == "left":
#         turn_left()
#     elif choice == "right":
#         turn_right()
#     elif choice == "around":
#         turn_around()
#     elif choice == "forward":
#         tim.forward(10)

steps = 5

for i in range(0, 360, steps):
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    tim.pencolor((R, G, B))
    tim.circle(100)
    tim.right(steps)



screen = Screen()
screen.exitonclick()