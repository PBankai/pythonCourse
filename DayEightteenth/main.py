import random
import turtle
from turtle import Turtle, Screen
import random
import colorgram
turtle.colormode(255)


def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tupple = (r, g, b)
    return my_tupple


tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(1)
tim.speed(0)

for k in range(180):
    tim.setheading(k*2)
    tim.color(randomcolor())
    tim.circle(100)

screen = Screen()
screen.exitonclick()
