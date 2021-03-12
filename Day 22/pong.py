from turtle import Screen, Turtle
from paddle import Paddle


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


game_is_on = True
while game_is_on:
    screen.update()


#TODO4: Create the ball and make it move

#TODO5: Detect collision with wall and bounce back

#TODO6: Detect collision with paddle

#TODO7: Detect when paddle misses the ball

#TODO8: Keep scores


screen.exitonclick()