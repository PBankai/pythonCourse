from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_left():
    new_heading_turtle = tim.heading() - 10
    tim.setheading(new_heading_turtle)


def move_right():
    new_heading_turtle = tim.heading() + 10
    tim.setheading(new_heading_turtle)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_right, "a")
screen.onkey(move_left, "d")
screen.onkey(clear, "c")

screen.exitonclick()
