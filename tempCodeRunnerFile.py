# main.py
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from roads_and_lights import RoadAndLights

screen = Screen()
screen.setup(width=1000, height=600)
screen.tracer(0)

car_manager = CarManager()
road_and_lights = RoadAndLights()

screen.listen()
directions = ['r-l', 'l-r', 'b-t', 't-b']
game_is_on = True
counter = 0
i = 0
light_colors = ["red", "red", "red", "red"]  # [top-bottom, bottom-top, left-right, right-left]
light_timer = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car(directions[i])
    car_manager.move_cars(light_colors)

    # Update traffic light color
    light_timer += 1
    if light_timer > 50:
        light_timer = 0
        if light_colors == ["red", "red", "red", "red"]:
            light_colors = ["green", "red", "red", "red"]
        elif light_colors == ["green", "red", "red", "red"]:
            light_colors = ["red", "green", "red", "red"]
        elif light_colors == ["red", "green", "red", "red"]:
            light_colors = ["red", "red", "green", "red"]
        elif light_colors == ["red", "red", "green", "red"]:
            light_colors = ["red", "red", "red", "green"]
        else:
            light_colors = ["green", "red", "red", "red"]

        road_and_lights.update_traffic_lights(light_colors)

    counter += 1
    if counter == 100:
        counter = 0
        i += 1
        if i == 4:
            i = 0

screen.exitonclick()
