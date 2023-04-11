from turtle import Turtle


class Graphic:

    def __init__(self):
        self.score_1 = 0
        self.score_2 = 0
        self.draw_limitation()
        self.draw_line()

    def condition(self, new_x):
        if new_x > 650:
            self.score_2 += 1
        elif new_x < -650:
            self.score_1 += 1
        self.score_board()

    def score_board(self):
        limit = Turtle()
        limit.speed("fastest")
        limit.hideturtle()
        limit.penup()
        limit.pencolor("DarkGoldenrod1")
        limit.goto(0, 230)
        limit.clear()
        limit.write(arg=f"{self.score_2}       {self.score_1}", move=False, align="center", font=("Algerian", 52, "bold"))

    def draw_line(self):
        limit = Turtle()
        limit.speed("fastest")
        limit.hideturtle()
        limit.setheading(90)
        limit.penup()
        limit.pencolor("DarkOrange4")
        limit.goto(0, -300)
        limit.pensize(5)
        limit.pendown()
        while limit.ycor() < 300:
            limit.forward(12)
            limit.penup()
            limit.forward(8)
            limit.pendown()
        limit.penup()
        limit.goto(40, 0)
        limit.pendown()
        limit.circle(40)

    def draw_limitation(self):
        limit = Turtle()
        limit.speed("fastest")
        limit.hideturtle()
        limit.penup()
        limit.pencolor("DarkOrange4")
        limit.goto(600, -300)
        limit.pensize(5)
        limit.pendown()
        limit.goto(600, 300)
        limit.goto(-600, 300)
        limit.goto(-600, -300)
        limit.goto(600, -300)
