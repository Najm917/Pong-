from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scorebord
import time

#screen create
screen=Screen()
screen.setup(800,680)
screen.bgcolor("#2D1630")
screen.title("PONG")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()
sbord=Scorebord()

#listen screen/event
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()
  
#detect collision with wall
  if ball.ycor()>320 or ball.ycor()<-320:
    ball.bounce_y()
    
  if ball.distance(r_paddle) < 50 and ball.xcor() >325:
      ball.bounce_x()
      
  if ball.distance(l_paddle) < 50 and ball.xcor() >-370:
      ball.bounce_x()
  #detect R Paddle
  if ball.xcor()>390:
    ball.reset_position()
    sbord.l_point()
    
  #detect L Paddle  
  if ball.xcor()<-400:
    ball.reset_position()
    sbord.r_point()
      

    
  
screen.exitonclick()