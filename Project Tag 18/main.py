from turtle import *
from random import *

colormode(255)

color_list = [(183, 162, 135), (181, 151, 161), (123, 93, 72), (146, 164, 177), (122, 81, 93), (52, 17, 27), (144, 171, 161), (16, 26, 43), (43, 23, 14), (76, 101, 117), (73, 110, 97), (14, 35, 24), (210, 201, 153), (153, 142, 78), (106, 39, 54), (216, 177, 187), (161, 108, 122), (170, 204, 193), (95, 145, 131), (164, 112, 102), (219, 179, 172), (107, 44, 36), (34, 82, 64), (183, 188, 208), (50, 57, 89), (77, 74, 35), (168, 202, 208), (92, 142, 149), (115, 122, 148), (31, 80, 88)]

timmy = Turtle()
timmy.speed("fastest")
my_screen = Screen()
my_screen.setworldcoordinates(-300, -300, 300, 300)
x_coor = -210
y_coor = -210


for j in range(0, 10):
    timmy.ht()
    ver = j*50
    timmy.penup()
    timmy.setposition(x_coor, y_coor + ver)
    timmy.st()
    for i in range(0, 9):
        ran_color = choice(color_list)
        timmy.pendown()
        timmy.dot(20, ran_color)
        timmy.penup()
        timmy.forward(50)
        ran_color = choice(color_list)
        timmy.pendown()
        timmy.dot(20, ran_color)


my_screen.exitonclick()