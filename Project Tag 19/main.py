from turtle import *
from random import *

color_bank = ["blue", "green", "yellow", "red", "black", "silver", "gold"]


my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your Bet", prompt="Which turtle will win the race ?")
race_on = True
turtle_bank= []

for index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_bank[index])
    new_turtle.setposition(x=-230, y=-145 + index*50)
    turtle_bank.append(new_turtle)

while race_on:
    for turtle in turtle_bank:
        ran_distance = randint(0, 10)
        turtle.forward(ran_distance)
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()

print(f"\n The Winner ist the turtle {winner}\n")
if user_bet == winner:
    print("you bet on the right turtle, you won")
else:
    print("you have lost")



my_screen.exitonclick()