from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen=Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME HEHE")
screen.tracer(0)

snk=Snake()
sc=Score()

food=Food()
screen.listen()

screen.onkey(snk.up,"Up")
screen.onkey(snk.down,"Down")
screen.onkey(snk.left,"Left")
screen.onkey(snk.right,"Right")


game_on=True

while game_on:
    screen.update()
    snk.move()
    time.sleep(0.1)



    if snk.head.distance(food) < 20:
        food.refresh()
        sc.score_plus()
        snk.add_snake()

    if snk.head.xcor() > 280 or snk.head.xcor() < -280 or snk.head.ycor() < -280 or snk.head.ycor() > 280:
        game_on=False
        sc.game_over()


    for k in snk.seg:
        if k==snk.head:
            pass
        elif snk.head.distance(k) < 10:
            game_on=False
            sc.game_over()




screen.exitonclick()
