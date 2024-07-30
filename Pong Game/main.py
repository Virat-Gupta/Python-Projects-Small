from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

ball = Ball()

scoreboard = Scoreboard()


screen.listen()
# screen.onkey(go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(l_paddle.go_down,"s")
screen.onkeypress(l_paddle.go_up,"w")


is_game_on = True

while is_game_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce
        ball.bounce_y()
    
    #detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320  or ball.distance(l_paddle) < 50 and ball.xcor() < -320  :
        ball.bounce_x()
    
    #detect when R paddle miss
    if (ball.xcor() > 380):
        ball.reset_position()
        scoreboard.l_point()

    if (ball.xcor() < -380):
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()