from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def level_up(self):
        self.level += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("Game OVER!", align="center", font=FONT)