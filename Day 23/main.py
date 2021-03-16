import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


#TODO1: Create the turtle and move it with keypress
player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")


#TODO2: Create and move cars
cars = CarManager()


#TODO5: Create a scoreboard
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()

    #TODO3: Detect turtle collission with cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #TODO4: Detect when turtle crosses the finish line
    if player.is_at_finish():
        player.goto_start()
        cars.level_up()
        scoreboard.level_up()


screen.exitonclick()