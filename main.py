from turtle import Screen , Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time




screen = Screen()
screen.setup(width= 600 , height = 600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

#adding boundary
mypen = Turtle()
mypen.penup()
mypen.setposition(-260,-260)
mypen.pendown()
mypen.color("red")
mypen.pensize(3)
mypen.fillcolor("grey")
mypen.begin_fill()
for side in range(4):
    mypen.forward(520)
    mypen.left(90)
mypen.end_fill()
mypen.hideturtle()





snake = Snake()

snake_food = Food()

scoreboard = Scoreboard()

user_input = screen.textinput("level", "choose your level of difficulty , easy / medium / hard")
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
easy_speed = 0.1
medium_speed = 0.10
hard_speed = 0.07

while game_is_on:

    if user_input == "easy":
        screen.update()
        time.sleep(easy_speed)
        snake.move()

    elif user_input == "medium":
        screen.update()
        time.sleep(medium_speed)
        snake.move()

    elif user_input == "hard":
        screen.update()
        time.sleep(hard_speed)
        snake.move()


    if snake.head.distance(snake_food) < 15:
        snake_food.refresh()
        snake.extend_segment()
        scoreboard.adding_score()
        if user_input == "easy":
            easy_speed -= 0.001
        elif user_input == "medium":
            medium_speed -= 0.001
        elif user_input == "hard":
            hard_speed -= 0.001


    def play_again():
        play_again = screen.textinput(title='Play Again?', prompt='Would you like to play again? (yes/no)')
        if play_again.lower() == 'yes':
            snake.reset_snake()
            screen.listen()
            return True
        elif play_again.lower() == 'no':
            screen.bye()

    if (snake.head.xcor() > 255 or snake.head.xcor() < -255 or snake.head.ycor() > 255
            or snake.head.ycor() < -255):
        scoreboard.game_end()
        if play_again():
            scoreboard.reset()
            scoreboard.hideturtle()
            scoreboard = Scoreboard()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            scoreboard.game_end()
            if play_again():
                scoreboard.reset()
                scoreboard.hideturtle()
                scoreboard = Scoreboard()


screen.exitonclick()