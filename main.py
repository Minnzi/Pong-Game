from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

game_is_on = True
game_screen = Screen()
game_screen.bgcolor("black")
game_screen.setup(width=800, height=600)
game_screen.title("Pong Game")
game_screen.tracer(0)
game_screen.listen()

l_paddle = Paddle(-380)
r_paddle = Paddle(375)
ball = Ball()
scoreboard = ScoreBoard()


game_screen.onkey(key="Up", fun=r_paddle.move_up)
game_screen.onkey(key="Down", fun=r_paddle.move_down)
game_screen.onkey(key="w", fun=l_paddle.move_up)
game_screen.onkey(key="s", fun=l_paddle.move_down)

while game_is_on:
    game_screen.update()
    time.sleep(0.1)
    ball.move()
    scoreboard.write_score(r_paddle.score, l_paddle.score)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle) < 50 and ball.xcor() < -365:
        ball.bounce()
        ball.increase_speed()
    if ball.xcor() > 400:
        ball.reset_position()
        l_paddle.increase_score()
    if ball.xcor() < -400:
        ball.reset_position()
        r_paddle.increase_score()
game_screen.exitonclick()
