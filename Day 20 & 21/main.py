from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)


#TODO5: Create scoreboard
scoreboard = Scoreboard()


#TODO1: Create the snake body
snake = Snake()


#TODO4: Detect collision with food
food = Food()


#TODO3: Control the snake
screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


#TODO2: Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()

        #Extend the snake size
        snake.extend()

        #Increase score when the snake hits the food
        scoreboard.increase_score()


    #TODO6: End game (Collision with wall)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    #TODO7: End game (Collision with tail)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()