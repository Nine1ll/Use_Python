import turtle
from turtle import Turtle, Screen
# import turtle as t
import random

turtle.colormode(255)
tim = Turtle()
tim.speed(0)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue,)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

# for _ in range(100):
#     direc = random.choice(direction)
#     tim.right(direc)
#     tim.forward(distance)
#     tim.color(random_color())

# def draw_dotted_line():
#     for i in range(10):
#         if i % 2 == 0:
#             tim.penup()
#         else:
#             tim.pendown()
#         tim.forward(10)
#
#
# def draw_angular_form(n):
#     for j in range(1, n+1):
#         tim.pendown()
#         tim.forward(100)
#         tim.right(360/n)
#
#
# # for _ in range(4):
# #     draw_dotted_line()
# #     tim.right(90)
# for i in range(3, 10+1):
#     draw_angular_form(i)

screen = Screen()
screen.exitonclick()

