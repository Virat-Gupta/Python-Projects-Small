from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_Score()

    def update_Score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="Center", font = ("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="Center", font = ("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_Score()


    def r_point(self):
        self.r_score += 1
        self.update_Score()