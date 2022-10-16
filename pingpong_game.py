import turtle

wn = turtle.Screen()
wn.title("Ping by Nirmal")
wn.bgcolor("Blue")
wn.setup(width=800, height=600)
wn.tracer(0)


# main 

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_a.penup() 
paddle_a.goto(-350,0)

# pad B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_b.penup() 
paddle_b.goto(350,0)
# ball
ball = turtle.Turtle()
ball.speed(-90)
ball.shape("square")
ball.color("white")
ball.penup() 
ball.goto(0,0)
ball.dx = 2
ball.dy = -2




# function to start the game

def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "e")
wn.onkeypress(paddle_b_down, "d")



while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor() + ball.dy)
# border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.setx(-390)
        ball.dx *= -1
# paddle and ba;; collisions
    if (ball.xcor() > 340 and ball.xcor()< 340) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1