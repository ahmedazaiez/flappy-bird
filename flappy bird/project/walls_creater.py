from turtle import Turtle ,colormode
import random
colormode(255)

class WallCreater:
    def __init__(self):
        self.walls=[]
        self.createWall()

    def createWall(self):
        r=random.randint(0, 255)
        g=random.randint(0, 255)
        b=random.randint(0, 255)
        wall_1=Turtle()
        wall_1.penup()
        wall_1.shape("square")
        wall_1.color(r,g,b)
        wall_1.shapesize(stretch_wid=20, stretch_len=2)
        y_cor= random.randint(-400, -100) 
        wall_1.goto(500,y_cor)
        wall_2=Turtle()
        wall_2.penup()
        wall_2.shape("square")
        wall_2.color((r,g,b))
        wall_2.shapesize(stretch_wid=20, stretch_len=2)
        wall_2.goto(500,y_cor + 500)
        self.new_wall=[]
        self.new_wall.append(wall_1)
        self.new_wall.append(wall_2)
        self.walls.append(self.new_wall)
    def move_walls(self):
        for walls in self.walls:
            walls[0].backward(5)
            walls[1].backward(5)
    def refresh_wall(self):
        if self.walls[-1][0].xcor()<300:
            self.createWall()
