from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.sety(250)
        self.color("White")

    def write_score(self, r_score, l_score):
        self.clear()
        self.write(arg=f"{l_score}     {r_score}", align="center", font=("Courier", 30, "bold"))

