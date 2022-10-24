import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()        
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5 )
        self.color("black")
        self.penup()
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
        self.speed("fastest")
    def change(self):
        self.shape("circle") 
        self.shapesize(stretch_len=0.5, stretch_wid=0.5 )
        self.color("black")
        self.penup()
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
        self.speed("fastest")       
    
    