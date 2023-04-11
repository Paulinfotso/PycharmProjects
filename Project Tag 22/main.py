from turtle import Screen
from graphic import Graphic
from pong import Player
from ball import Ball
from time import sleep

my_screen = Screen()
my_screen.title("My Pong Game")
my_screen.screensize(canvwidth=1200, canvheight=600, bg="burlywood4")

graphic = Graphic()
player = Player()
my_screen.listen()
my_screen.onkeypress(fun=player.up, key="8")
my_screen.onkeypress(fun=player.down, key="2")
my_screen.tracer(0)

ball = Ball()


game_on = True
while game_on:
    graphic.score_board()
    graphic.condition(new_x=ball.x)
    ball.collission_wall()
    player.mobility_2(new_x=ball.x, new_y=ball.y, head=ball.h)
    ball.collision_player(player.player_1, player.player_2)
    player.mobility_2(new_x=ball.x, new_y=ball.y, head=ball.h)

    if ball.x > 650 or ball.x < -650:
        player.reset()
        ball.reset()
        my_screen.update()
        sleep(7)
    my_screen.update()
    sleep(0.1)

my_screen.exitonclick()
