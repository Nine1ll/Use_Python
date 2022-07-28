from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.penup()
        self.left(90)
        self.goto(x=coordinates[0], y=coordinates[1])
        self.color("white")

    def up(self):
        if self.ycor()+MOVE_DISTANCE <= 240:
            self.goto(self.xcor(), y=self.ycor()+MOVE_DISTANCE)

    def down(self):
        if self.ycor()-MOVE_DISTANCE >= -240:
            self.goto(self.xcor(), y=self.ycor() - MOVE_DISTANCE)



