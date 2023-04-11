from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.setposition(0, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"score: {self.score}", True, align="center", font=("Arial", 21, "normal"))
        self.setposition(0, 280)

    def refresh(self):
        self.score += 1
        self.clear()
        self.update_score()
