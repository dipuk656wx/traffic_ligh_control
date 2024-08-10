# road_and_lights.py
from turtle import Turtle

class RoadAndLights:
    def __init__(self):
        self.road_turtle = Turtle()
        self.traffic_light_turtles = [Turtle() for _ in range(4)]
        self.setup()

    def setup(self):
        self.road_turtle.speed(0)
        self.road_turtle.penup()
        self.road_turtle.hideturtle()
        self.draw_road()
        
        for light_turtle in self.traffic_light_turtles:
            light_turtle.speed(0)
            light_turtle.penup()
            light_turtle.hideturtle()
        
        self.draw_traffic_lights()

    def draw_road(self):
        self.road_turtle.goto(-500, 300)
        self.road_turtle.pendown()
        self.road_turtle.goto(500, 300)
        self.road_turtle.goto(500, -300)
        self.road_turtle.goto(-500, -300)
        self.road_turtle.goto(-500, 300)

    def draw_traffic_lights(self):
        positions = [(200, 250), (-200, 250), (-200, -250), (200, -250)]
        for i, light_turtle in enumerate(self.traffic_light_turtles):
            light_turtle.goto(positions[i])
            light_turtle.pendown()
            light_turtle.color("black")
            light_turtle.begin_fill()
            light_turtle.circle(20)
            light_turtle.end_fill()
            light_turtle.hideturtle()

    def update_traffic_lights(self, colors):
        positions = [(200, 250), (-200, 250), (-200, -250), (200, -250)]
        for i, (color, pos) in enumerate(zip(colors, positions)):
            self.traffic_light_turtles[i].clear()
            self.traffic_light_turtles[i].goto(pos)
            self.traffic_light_turtles[i].color(color)
            self.traffic_light_turtles[i].begin_fill()
            self.traffic_light_turtles[i].circle(15)
            self.traffic_light_turtles[i].end_fill()
