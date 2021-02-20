# import colorgram

# rgb_colors = []
# colors = colorgram.extract('Day 18\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")

color_list = [(139, 164, 183), (21, 118, 177), (240, 213, 59), (204, 139, 166), (223, 158, 84), (122, 72, 98), (142, 20, 36), (20, 138, 58), (190, 175, 23), (71, 30, 36), (195, 72, 33), (225, 171, 198), (57, 35, 32), (25, 170, 184), (236, 85, 33), (7, 111, 66), (109, 190, 136), (42, 173, 81), (183, 94, 110), (188, 183, 210), (39, 38, 45), (156, 208, 216), (154, 213, 175), (241, 171, 151), (229, 212, 16), (125, 115, 160)]

tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)

numer_of_dots = 101

for dot_count in range(1, numer_of_dots):
    tim.dot(28, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if(dot_count % 10 == 0):
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()