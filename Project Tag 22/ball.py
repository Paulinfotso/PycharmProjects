from turtle import Turtle
from random import randint, choice
start_orientation = randint(152, 165)


class Ball:

    def __init__(self):
        self.ball = Turtle(shape="circle")
        self.ball.penup()
        self.h = 0
        self.x = 0
        self.y = 0
        self.ball.color("DarkSeaGreen")
        self.ball.setheading(start_orientation)

    def collission_wall(self):
        self.ball.forward(20)
        direction = self.ball.heading()
        if self.ball.ycor() > 290 or self.ball.ycor() < -290:
            self.ball.setheading(360-direction)

    def collision_player(self, player_1, player_2):
        self.ball.forward(20)
        direction = self.ball.heading()
        if self.ball.distance(player_1) < 50:
            if 0 < direction < 90:
                self.ball.setheading(180 - direction)
            elif 270 < direction < 360:
                self.ball.setheading(540 - direction)
        elif self.ball.distance(player_2) < 50:
            if 90 < direction < 180:
                self.ball.setheading(180 - direction)
            elif 180 < direction < 270:
                self.ball.setheading(540 - direction)
        self.x = self.ball.xcor()
        self.y = self.ball.ycor()
        self.h = self.ball.heading()

    def reset(self):
            self.ball.goto(0, 0)
            ran = [1, 0, -1, 2]
            if choice(ran) == 1:
                self.ball.setheading(randint(195, 206))
            elif choice(ran) == 0:
                self.ball.setheading(randint(152, 165))
            elif choice(ran) == -1:
                self.ball.setheading(randint(15, 28))
            else:
                self.ball.setheading(randint(332, 345))
