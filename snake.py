from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0




class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        x_index = 0
        for turtle_index in range(0, 3):
            turtle_object = Turtle(shape="square")
            turtle_object.color("white")
            turtle_object.penup()
            self.segments.append(turtle_object)
            turtle_object.goto(0 + x_index, 0)
            x_index -= 20
    def move(self):
        
            for seg_num in range(2, 0,-1):
                new_x = self.segments[seg_num -1].xcor()
                new_y = self.segments[seg_num -1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(20)
    def up(self):
         if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)
    def down(self):
         if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)
    def left(self):
         if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)
    def right(self):
         if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)
