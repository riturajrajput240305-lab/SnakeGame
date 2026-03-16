from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WALL_BOUNDARY = 280
FOOD_COLLISION_DISTANCE = 15
TAIL_COLLISION_DISTANCE = 10

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < FOOD_COLLISION_DISTANCE:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > WALL_BOUNDARY
        or snake.head.xcor() < -WALL_BOUNDARY
        or snake.head.ycor() > WALL_BOUNDARY
        or snake.head.ycor() < -WALL_BOUNDARY
    ):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < TAIL_COLLISION_DISTANCE:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()