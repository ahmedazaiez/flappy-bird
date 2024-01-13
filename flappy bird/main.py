from turtle import Screen
from player import Player
from walls_creater import WallCreater
import time 
from scoreboard import Scoreboard


screen=Screen() 
screen.setup(800,600)
screen.tracer(0) 

player=Player()
wall=WallCreater()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.jump, " ")

game_is_on= True

while game_is_on: 
    time.sleep(0.1)
    player.fall()
    wall.refresh_wall()
    wall.move_walls()
    for w in wall.walls:
        if player.xcor()+10 >= w[0].xcor()-20 and player.xcor()-10 <= w[0].xcor()+20:
            
            if player.ycor()-10<=w[0].ycor()+200 or player.ycor()+10>=w[1].ycor()-200:
                scoreboard.game_ove()
                game_is_on= False
        if player.xcor()==w[0].xcor():
            scoreboard.increase_score()
    screen.update() 

screen.exitonclick()