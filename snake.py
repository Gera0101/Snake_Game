from turtle import Screen, Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]
back = 270
font = 180
left = 90
right = 0
class Snake():
    def __init__(self):
        self.snk = []
        self.screen = Screen()
    def snake_maker(self):
        for i in POSITION:
            self.add(i)
    def add(self, i):
        self.snakes = Turtle()
        self.snakes.penup()
        self.snakes.shape("square")
        self.snakes.color("black")
        self.snakes.goto(i)
        self.snk.append(self.snakes)
    def extent(self):
        self.add(self.snk[-1].position())
    def move(self): 
        imena = self.snk[0]
        for i in range(len(self.snk) - 1, 0, -1):
            self.x = self.snk[i - 1].xcor()
            self.y = self.snk[i - 1].ycor()
            self.snk[i].goto(self.x, self.y)  
        def a():
            if imena.heading() != left:        
               imena.setheading(back)
        def d():
            if imena.heading() != right:
               imena.setheading(font)
        def c():
            if imena.heading() != font:
               imena.setheading(right)
        def b():
            if imena.heading() != back:
               imena.setheading(left)
        screen = Screen()
        screen.onkey(a, "Down")
        screen.onkey(b, "Up")
        screen.onkey(c, "Right")
        screen.onkey(d, "Left")
        imena.forward(10)
        screen.listen()
        