from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bed", prompt="Which turtle will win the race?")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
for turtle_index in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-235, y=-70 + turtle_index * 30)
    new_turtle.color(colors[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won  the {winning_color} turtle is the winner")
            else:
                print(f"You've lost  the {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
