from turtle import Turtle
import random

FD_CLR="yellow"
FD_SP="circle"
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FD_SP)
        self.penup()
        self.color(FD_CLR)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        self.goto(x,y)
