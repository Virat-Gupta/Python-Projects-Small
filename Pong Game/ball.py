from turtle import Turtle

class Ball(Turtle):
    def __init__(self) :
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_X = self.xcor() + self.x_move
        new_Y = self.ycor() + self.y_move
        self.goto(new_X,new_Y)

    def bounce_y(self):
        self.y_move = -self.y_move
        self.move_speed *= 0.95

    def bounce_x(self):
        self.x_move = -self.x_move
        self.move_speed *= 0.95
    
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.05
