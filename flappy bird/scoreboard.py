from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(-250,230)
        self.write_score()
          
    def write_score(self):   
        self.clear()
        self.write(f"Score:{self.score}",align="center", font=("Courier",30,"bold"))

    def increase_score(self):
        self.score+=1
        self.write_score()
    
    def game_ove(self):
        self.goto(0,0)
        self.write("GAME OVER!!!" ,align="center", font=("Courier",60,"bold"))