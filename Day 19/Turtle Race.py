from turtle import Turtle, Screen
import random


is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "purple", "green", "blue"]
y_coordinates = [-100, -60, -20, 20, 60, 100]
all_turtle = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_coordinates[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_game_on = True


while  is_game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 222:
            is_game_on = False
            winning_turtle = turtle.pencolor()

            if winning_turtle == user_bet:
                print(f"You won! The {winning_turtle} turtle won the race.")
            else:
                print(f"You lost! The {winning_turtle} turtle won the race.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()