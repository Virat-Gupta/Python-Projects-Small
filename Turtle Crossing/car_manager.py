from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self) -> None:
        self.car_list = []

    def generate_car(self):
        new_car = Car()
        self.car_list.append(new_car)
        rand_Y = random.randint(-250,250)
        new_car.goto(320,rand_Y)
    
    def move_cars(self):
        for car in self.car_list:
            car.goto(car.xcor() - MOVE_INCREMENT, car.ycor())

    def detect_collision(self, player) -> bool:
        for car in self.car_list:
            if car.distance(player) < 20 : 
                return True
        return False
    
    def next_level(self):
        for car in self.car_list:
            car.hideturtle()
        self.car_list.clear()


class Car(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.penup()