from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")

#TODO1: Create the snake body
starting_position = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)

#TODO2: Move the snake

#TODO3: Control the snake

#TODO4: Detect collision with food

#TODO5: Create scoreboard

#TODO6: End game (Collision with wall)

#TODO7: End game (Collision with tail)

screen.exitonclick()