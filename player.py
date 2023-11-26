import random
from turtle import Turtle


class Player(Turtle):
    import colors

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color(random.choice(self.colors.COLORS))
        self.goto(x=0, y=-240)
        self.setheading(90)
        self.shapesize(2, 2)

    def go_up(self):
        self.forward(40)

    def go_down(self):
        self.backward(40)

    def rest_position(self):
        self.goto(x=0, y=-240)

    def at_finish(self):
        if self.ycor() > 250:
            return True
        else:
            return False



