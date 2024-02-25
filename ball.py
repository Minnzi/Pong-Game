from turtle import Turtle
STARTING_PACE = 10
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.penup()
        self.setheading(45)
        self.pace = STARTING_PACE
    def bounce(self):
        current_heading = self.heading()
        self.setheading(current_heading - 90)

    def reset_position(self):
        if self.xcor() > 400:
            self.setheading(225)
        else:
            self.setheading(45)
        self.goto(0,0)
        self.pace = STARTING_PACE

    def move(self):
        self.forward(self.pace)

    def increase_speed(self):
        self.pace += 5
        self.forward(self.pace)