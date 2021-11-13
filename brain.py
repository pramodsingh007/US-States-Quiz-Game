from turtle import Turtle

name =  Turtle()
class Brain():
    def __init__(self):
        name.color("black")
        name.penup()
        name.hideturtle()
        name.speed("fastest")

    def show_states(self,x_position,y_position,city_name):         #this function will shows up name of states on the mapp
        name.goto(x_position,y_position)
        name.write(arg=city_name,font=("Courier",8,"normal"))    