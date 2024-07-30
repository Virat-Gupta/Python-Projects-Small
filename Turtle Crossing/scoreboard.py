from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_Score()
    
    def update_Score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level : {self.level}", align="Center", font = FONT)
    
    def next_level(self):
        self.level += 1
        self.update_Score()


