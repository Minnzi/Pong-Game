from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.penup()
        self.setx(position)
        self.score = 0

    def move_up(self):
        self.forward(30)

    def move_down(self):
        self.backward(20)

    def increase_score(self):
        self.score += 1

