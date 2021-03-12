from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


#TODO1: Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.listen()
screen.tracer(0) # Disableing the animations


#TODO2: Create a moving paddle
r_paddle = Paddle((350, 0))
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


#TODO3: Create another moving paddle
l_paddle = Paddle((-350, 0))
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


#TODO4: Create the ball and make it move
ball = Ball()


#TODO8: Keep scores
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #TODO5: Detect collision with wall and bounce back
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Bounce the ball
        ball.bounce_y()

    #TODO6: Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #TODO7: Detect when paddle misses the ball
    # Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()