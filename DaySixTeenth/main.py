import turtle

import prettytable

Timmy = turtle.Turtle()
print(Timmy)
Timmy.shape("turtle")
Timmy.color("coral")
Timmy.forward(100)
my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = prettytable.PrettyTable()
table.add_column("Pokemon", ["Pikachu","Lucario","Groundon"])
print(table)