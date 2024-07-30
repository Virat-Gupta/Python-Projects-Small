from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-280)
    
    def move_up(self):
        new_Y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_Y)

    def move_down(self):
        if (self.ycor() < -290):
            return
        new_Y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_Y)

    def next_level(self):
        self.goto(x=0, y=-280)

