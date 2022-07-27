from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.color("white")
        self.updata_scoreboard()

    def updata_scoreboard(self):
        self.write(arg=f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.updata_scoreboard()
    # def reshow(self):
    #     self.clear()
    #     self.write(arg=f"Score : {self.score}", align="center", font=('Arial', 18, "normal"))



