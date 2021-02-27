from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)


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


#TODO5: Create scoreboard

#TODO6: End game (Collision with wall)

#TODO7: End game (Collision with tail)

screen.exitonclick()