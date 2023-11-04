from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)

