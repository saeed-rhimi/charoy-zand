import time
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.lives = 2
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 220)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 15, "bold"))
        self.goto(300, 220)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 15, "bold"))

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def loose_life(self):
        self.lives -= 1
        self.update_scoreboard()
        time.sleep(1)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game over", align="center", font=("Courier", 30, "bold"))
        self.goto(0, 40)
        self.write(f"Max Level: {self.level}", align="center", font=("Courier", 30, "bold"))

