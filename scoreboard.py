from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.gera = super()
        self.gera.penup()
        self.gera.goto(-5, 270)
        self.gera.hideturtle()
    def first_score(self, score):
        self.gera.write(f"Score: {score}", False, align="center", font=("Arial", 20, "normal"))
    def add_score(self, score):
        self.gera.write(f"Score: {score}", False, align="center", font=("Arial", 20, "normal"))
  