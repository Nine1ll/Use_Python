from turtle import Turtle
FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 260)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",  align=ALIGNMENT, font=FONT)
