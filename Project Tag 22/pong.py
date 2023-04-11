from turtle import Turtle


class Player:

    def __init__(self):
        self.player_1 = Turtle(shape="square")
        self.player_1.penup()
        self.player_1.color("blue")
        self.player_1.goto(600, 0)
        self.player_1.setheading(90)
        self.player_1.shapesize(stretch_len=5, stretch_wid=1)
        self.player_2 = Turtle(shape="square")
        self.player_2.setheading(90)
        self.player_2.penup()
        self.player_2.color("red")
        self.player_2.goto(-600, 0)
        self.player_2.shapesize(stretch_len=5, stretch_wid=1)

    def up(self):
        if self.player_1.ycor() < 265:
            self.player_1.forward(20)

    def down(self):
        if self.player_1.ycor() > -265:
            self.player_1.backward(20)

    def mobility_2(self, new_x, new_y, head):
        if new_x < 450 and 90 < head < 180:
            if self.player_2.ycor() < new_y:
                self.player_2.forward(20)
        elif new_x < 450 and 180 < head < 270:
            if self.player_2.ycor() > new_y:
                self.player_2.backward(20)

    def reset(self):
        self.player_2.goto(-600, 0)
        self.player_1.goto(600, 0)
