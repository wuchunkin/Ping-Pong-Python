#Simple Pythong 3 , ping pong game
# turtle module for biginners
import turtle
#Create screen
wn = turtle.Screen()
wn.title('Pong by Anvarbey.muminov@gmail.com')
wn.bgcolor('black')
wn.setup(width = 800, height =600)
wn.tracer(0)
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid = 5,stretch_len =1);
paddle_a.penup()
paddle_a.goto(-350,0)
#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.shapesize(stretch_wid = 5,stretch_len =1);
paddle_b.penup()
paddle_b.goto(350,0)
#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color('white')
#ball.shapesize(stretch_wid = 5,stretch_len =1);
ball.penup()
ball.goto(0,0)
ball.dx = 1 #everytime ball moves , it moves by 1 px
ball.dy = 1
#function creation for paddle_a
def paddle_a_up():
  y = paddle_a.ycor() #return y cordinate
  y += 20
  paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor() #return y cordinate
  y -= 20
  paddle_a.sety(y)
#Function creation  for paddle_b
def paddle_b_up():
  y = paddle_b.ycor() #return y cordinate
  y += 20
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor() #return y cordinate
  y -= 20
  paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkey(paddle_a_up,"w")
wn.onkey(paddle_a_down,"s")
wn.onkey(paddle_b_up,"Up")
wn.onkey(paddle_b_down,"Down")




#Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() +ball.dx)
    ball.sety(ball.ycor() +ball.dy)

    # Border checking Up
    if ball.ycor() > 290:
      ball.sety(290)
      ball.dy *= -1
    # Border checking Down
    if ball.ycor() < - 290:
      ball.sety(-290)
      ball.dy *= -1
     # Border checking Left
    if ball.xcor() > 390:
      ball.goto(0,0)
      ball.dx *= -1
    if ball.xcor() < -390:
      ball.goto(0,0)
      ball.dx *= -1

     # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
       # os.system("afplay bounce.wav&")

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
       # os.system("afplay bounce.wav&")
