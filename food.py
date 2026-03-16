from turtle import Turtle
import random

GRID_SIZE = 20
FOOD_BOUNDARY = 14


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-FOOD_BOUNDARY, FOOD_BOUNDARY) * GRID_SIZE
        random_y = random.randint(-FOOD_BOUNDARY, FOOD_BOUNDARY) * GRID_SIZE
        self.goto(random_x, random_y)
