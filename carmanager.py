from turtle import Turtle
import random
import colors


class CarManager:
    MOVE_SPEED = 5
    SPEED_STEP = 10

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle()
            new_car.setheading(180)
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.goto(x=400, y=random.randint(-250, 250))
            new_car.color(random.choice(colors.COLORS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.MOVE_SPEED)

    def increase_speed(self):
        self.MOVE_SPEED += self.SPEED_STEP
