from telnetlib import PRAGMA_HEARTBEAT
import time
from food import Food
from snake import Snake
from scoreboard import Score
from turtle import Screen, Turtle
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My snake game")
screen.tracer(0)
over = Turtle()
over.hideturtle()
over.penup()
def overgame():
    over.write("GAME OVER!", False, align="center", font=("Arial", 18, "normal"))
game = True
scr = Score()  
score = 0
scr.first_score(score)
fod = Food()
snake = Snake()
snake.snake_maker()
while game:
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.snakes.distance(fod) < 15:
        fod.change()
        snake.extent()
        score += 1
        scr.gera.clear()
        scr.add_score(score)
    if snake.snakes.xcor() > 280 or snake.snakes.xcor()  < -280 or snake.snakes.ycor() > 280 or snake.snakes.ycor()  < -280:
        game = False  
        overgame()
    for i in snake.snk:
        if i == snake.snk[0]:
            pass
        elif snake.snk[0].distance(i) < 10:
            overgame()
            game = False
screen.exitonclick()

