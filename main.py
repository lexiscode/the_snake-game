from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # hides the turtle pendown lines

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
    # this hides the turtle scenes/steps, and displays only the final output scenes
    # delay 0.25 seconds, then refresh the screen
    screen.update()
    time.sleep(0.25)  # in this case, it can as well be used to determine snake's speed

    snake.move()  # the snake should move forwards by 1-step

    # Detect collision with food
    # recall the food size is 10 by 10, so we assume once the snake-head distance is close to 10,
    # that is less than 15, it should trigger food.refresh()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # if snake-head collides with any segment in the tail, trigger game over
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    # alternatively, below
    '''
    for segment in snake.segments[1:]:  # slicing
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    '''


screen.exitonclick()
