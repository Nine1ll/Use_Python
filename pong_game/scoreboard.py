from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 60, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.penup()

        self.l_score = 0
        self.r_score = 0
        self.updata_scoreboard()

    def updata_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)

        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

        self.goto(0, 210)
        self.write(":", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1

        self.updata_scoreboard()

    def r_point(self):
        self.r_score += 1

        self.updata_scoreboard()

