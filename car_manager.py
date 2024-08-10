# car_manager.py
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.tb_cars = []
        self.bt_cars = []
        self.lr_cars = []
        self.rl_cars = []
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.directions = {'t-b': self.tb_cars, 'b-t': self.bt_cars, 'l-r': self.lr_cars, 'r-l': self.rl_cars}

    def create_car(self, direction):
        random_chance = random.randint(1, 10)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            randon_x = random.randint(-40, 40)

            if direction == 't-b':
                new_car.goto(randon_x, 300)
                new_car.right(90)
                self.tb_cars.append(new_car)
            elif direction == 'l-r':
                new_car.goto(-300, randon_x)
                self.lr_cars.append(new_car)
            elif direction == 'r-l':
                new_car.goto(300, randon_x)
                new_car.right(180)
                self.rl_cars.append(new_car)
            elif direction == 'b-t':
                new_car.goto(randon_x, -300)
                new_car.left(90)
                self.bt_cars.append(new_car)

            self.all_cars.append(new_car)

    def move_cars(self, colors):
        for direction, cars in self.directions.items():
            if (direction == 't-b' and colors[0] == 'green') or \
               (direction == 'b-t' and colors[1] == 'green') or \
               (direction == 'l-r' and colors[2] == 'green') or \
               (direction == 'r-l' and colors[3] == 'green'):
                for car in cars:
                    car.forward(self.car_speed)
            else:
                for car in cars:
                    car.hideturtle()

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def delete_car(self):
        if self.all_cars:
            self.all_cars.pop(0)
