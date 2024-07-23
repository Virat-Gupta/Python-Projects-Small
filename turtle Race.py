from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="MAKE BET", prompt="WHICH TURTLE ??? TELL COLOR ASAP:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
distanceBW = 50
topY = int(2.5*distanceBW)
for i in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y = topY)
    topY -= distanceBW
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            win_color = turtle.pencolor()
            if (win_color == user_bet):
                print(f"You WON!. The winning color is {win_color}.")
            else:
                print(f"You LOST!. The winning color is {win_color}.")
            is_race_on = False
            break;
        turtle.fd(random.randint(1,10))

screen.exitonclick()