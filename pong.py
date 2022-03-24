import turtle

wn = turtle.Screen()
wn.title("Ping Pong By Nick")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
count_a, count_b = 0,0

# Bat A
bat_a = turtle.Turtle()
bat_a.speed(0)
bat_a.shape("square")
bat_a.color("red")
bat_a.shapesize(stretch_wid=5, stretch_len=1)
bat_a.penup()
bat_a.goto(-350,0)

# Bat B
bat_b = turtle.Turtle()
bat_b.speed(0)
bat_b.shape("square")
bat_b.color("yellow")
bat_b.shapesize(stretch_wid=5, stretch_len=1)
bat_b.penup()
bat_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.04
ball.dy = 0.04

# Move Bat A
def bat_a_up():
    y = bat_a.ycor()
    y += 20
    bat_a.sety(y)

def bat_a_down():
    y = bat_a.ycor()
    y -= 20
    bat_a.sety(y)

# Move Bat B
def bat_b_up():
    y = bat_b.ycor()
    y += 20
    bat_b.sety(y)

def bat_b_down():
    y = bat_b.ycor()
    y -= 20
    bat_b.sety(y)

# Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player 1 : {}  |  Player 2 : {}'.format(count_a,count_b), align = 'center', font = ("Courier", 24, "normal"))


# Keyboard binding
wn.listen()
wn.onkeypress(bat_a_up,'w')
wn.onkeypress(bat_a_down,'s')
wn.onkeypress(bat_b_up,'Up')
wn.onkeypress(bat_b_down,'Down')

while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boundary for the ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        count_a +=1
        pen.clear()
        pen.write('Player 1 : {}  |  Player 2 : {}'.format(count_a,count_b), align = 'center', font = ("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        count_b +=1
        pen.clear()
        pen.write('Player 1 : {}  |  Player 2 : {}'.format(count_a,count_b), align = 'center', font = ("Courier", 24, "normal"))

    # Bat and Ball Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bat_b.ycor() + 40 and ball.ycor() > bat_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bat_a.ycor() + 40 and ball.ycor() > bat_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1