from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 4


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.color(choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.x = 300
        self.y = randint(-250, 250)
        self.goto(self.x, self. y)
        self.setheading(180)


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if randint(1, 6) == 1:
            new_car = Car()
            self.cars.append(new_car)
            return True
        return False

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.clear_cars()
        self.car_speed += MOVE_INCREMENT

    def clear_cars(self):
        for car in self.cars:
            car.reset()
            car.hideturtle()
        self.cars = []
