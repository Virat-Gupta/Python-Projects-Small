import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")


car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
genDelay = 0

Level_Speed = 0.1

while game_is_on:
    time.sleep(Level_Speed)
    screen.update()

    #generate cars
    car_manager.move_cars()
    if genDelay > 6:
        car_manager.generate_car()
        genDelay = 0
    genDelay += 1


    #detect car collision
    if car_manager.detect_collision(player):
        game_is_on = False

    #detect Finished Level
    if player.ycor() > 280 :
        #increse level
        player.next_level()
        car_manager.next_level()
        scoreboard.next_level()
        Level_Speed *= 0.75


screen.exitonclick()
