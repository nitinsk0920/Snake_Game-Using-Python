from turtle import Turtle
SNAKE_POS=[(0,0),(-20,0),(-40,0)]
MOVE_SPEED=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
SN_COLOR="blue"
SN_SHAPE="circle"
class Snake:

    def __init__ (self):

        self.seg=[]
        self.create_snake()
        self.head=self.seg[0]

    def create_snake(self):
        for i in SNAKE_POS:
            snake=Turtle(SN_SHAPE)
            snake.color(SN_COLOR)
            snake.penup()
            snake.goto(i)
            self.seg.append(snake)

    def move(self):
        for j in range(len(self.seg)-1,0,-1):
            x=self.seg[j-1].xcor()
            y=self.seg[j-1].ycor()
            self.seg[j].goto(x,y)
        self.seg[0].forward(MOVE_SPEED)
    
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def add_snake(self):
        snake=Turtle(SN_SHAPE)
        snake.color(SN_COLOR)
        snake.penup()
        self.seg.append(snake)
        self.move()

    

