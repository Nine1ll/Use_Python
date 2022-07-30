from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=random.randint(2, 4))
            new_car.color(random.choice(COLORS))

            new_car.penup()
            new_car.goto(x=320, y=random.randint(-260, 260))
            new_car.move_speed = STARTING_MOVE_DISTANCE

            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            new_xcor = car.xcor() - car.move_speed
            car.goto(new_xcor, car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

