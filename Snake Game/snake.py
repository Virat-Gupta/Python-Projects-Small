from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        XPos = 0
        for _ in range(3):
            position =  (XPos,0)
            self.add_segment(position)
            XPos -= 20

    def add_segment(self,position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segment.append(new_turtle)
            
    def extend(self):
        self.add_segment(self.segment[-1].position())


    
    def move(self): 
        for index in range(len(self.segment)- 1,0,-1):
            newX = self.segment[index-1].xcor()
            newY = self.segment[index-1].ycor()
            self.segment[index].goto(newX,newY)
        self.head.forward(MOVE_DISTANCE)
    


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




