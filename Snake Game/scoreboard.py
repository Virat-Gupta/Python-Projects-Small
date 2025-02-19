from turtle import Turtle

ALIGN = "center"
FONT = ("Courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.score = 0
        with open("Snake Game\\data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} HighScore : {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self) :
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Snake Game\\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
    

