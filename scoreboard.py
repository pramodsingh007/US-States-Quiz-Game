from turtle import Turtle 

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("black")
        self.score = 0
    def update_score(self): 
        self.clear()
        self.goto(0,220)
        self.write(arg=f"points {self.score}",align="center",font=("Courier",20,"bold"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over",align="center",font=("Courier",30,"bold"))