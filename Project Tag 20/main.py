from turtle import Screen, Turtle
from time import sleep
from snake import Snake
from food import Food
from score import Score

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
game_on = True

my_screen = Screen()
my_screen.title("My Snake Game")
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

my_screen.listen()
my_screen.onkey(snake.right, "d")
my_screen.onkey(snake.left, "a")
my_screen.onkey(snake.up, "w")
my_screen.onkey(snake.down, "s")

while game_on:
    my_screen.update()
    sleep(0.1)
    snake.movement()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh()
        timmy = Turtle(shape="square")
        timmy.penup()
        snake.body.append(timmy)
        timmy.color("black", "white")

    game_on = snake.with_body()
    if game_on:
        game_on = snake.with_wall()

my_screen.exitonclick()
