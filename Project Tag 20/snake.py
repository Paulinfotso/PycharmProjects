from turtle import *

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


def over():

    writer = Turtle()
    writer.color("white")
    writer.hideturtle()
    writer.penup()
    writer.write("Game Over !", True, "center", font=("Arial", 14, "normal"))


class Snake:

    def __init__(self):
        self.start_position = [(0, 0), (-20, 0), (-40, 0)]
        self.body = []
        self.body_snake()
        self.head = self.body[0]

    def body_snake(self):
        print("Creation of the Body of your snake")
        for start in self.start_position:
            self.add_body(location= start)

    def add_body(self, location):
        new_turtle = Turtle(shape="square")
        new_turtle.speed("fastest")
        new_turtle.penup()
        new_turtle.color("black", "white")
        new_turtle.goto(location)
        self.body.append(new_turtle)

    def extend(self):
        self.add_body(self.body[-1].position)

    def movement(self):

        for element in range(len(self.body) - 1, 0, -1):
            new_x = self.body[element - 1].xcor()
            new_y = self.body[element - 1].ycor()
            self.body[element].goto(new_x, new_y)
        self.body[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.body[0].setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.body[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.body[0].setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.body[0].setheading(DOWN)

    def finish(self):
        writen = Turtle()
        writen.color("white")
        writen.hideturtle()
        writen.penup()
        writen.write("Game Over !", True, "center", font=("Arial", 21, "normal"))

    def with_wall(self):

        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            self.finish()
            return False
        else:
            return True

    def with_body(self):

        for element in self.body[1:]:

            if self.head.distance(element) < 10:
                self.finish()
                return False
            else:
                return True
