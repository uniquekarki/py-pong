import turtle

class Bat:
    def __init__(self,side):
        self.bat = turtle.Turtle()
        self.bat.speed(0)
        self.bat.shape("square")
        self.bat.color("white")
        self.bat.shapesize(stretch_wid=5, stretch_len=1)
        self.bat.penup()
        if side == 'a':
            self.bat.goto(-350,0)
        else:
            self.bat.goto(350,0)

    def bat_up(self):
        y = self.bat.ycor()
        y += 20
        self.bat.sety(y)

    def bat_down(self):
        y = self.bat.ycor()
        y -= 20
        self.bat.sety(y)


class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0,0)
        self.ball.dx = 0.06
        self.ball.dy = 0.06


        self.count_a = 0
        self.count_b = 0
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color('white')
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0,260)
        self.pen.write('Player 1 : {}  |  Player 2 : {}'.format(count_a,count_b), align = 'center', font = ("Courier", 24, "normal"))

    def move_ball(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1

        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1
        
        if self.ball.xcor() > 390:
            self.ball.goto(0,0)
            self.ball.dx *= -1
            self.count_a += 1
            self.pen.clear()
            self.pen.write('Player 1 : {}  |  Player 2 : {}'.format(self.count_a,self.count_b), align = 'center', font = ("Courier", 24, "normal"))
            
        if self.ball.xcor() < -390:
            self.ball.goto(0,0)
            self.ball.dx *= -1
            self.count_b +=1
            self.pen.clear()
            self.pen.write('Player 1 : {}  |  Player 2 : {}'.format(self.count_a,self.count_b), align = 'center', font = ("Courier", 24, "normal"))

if __name__ == '__main__':
    wn = turtle.Screen()
    wn.title("Ping Pong By Nick")
    wn.bgcolor("black")
    wn.setup(width = 800, height= 600)
    wn.tracer(0)
    count_a, count_b = 0,0


    bat_a = Bat("a")
    bat_b = Bat("b")
    ball = Ball()

    wn.listen()
    wn.onkeypress(bat_a.bat_up,'w')
    wn.onkeypress(bat_a.bat_down,'s')
    wn.onkeypress(bat_b.bat_up,'Up')
    wn.onkeypress(bat_b.bat_down,'Down')


    while True:
        wn.update()

        ball.move_ball()

        # Bat and Ball Collision
        if (ball.ball.xcor() > 340 and ball.ball.xcor() < 350) and (ball.ball.ycor() < bat_b.bat.ycor() + 40 and ball.ball.ycor() > bat_b.bat.ycor() - 40):
            ball.ball.setx(340)
            ball.ball.dx *= -1

        if (ball.ball.xcor() < -340 and ball.ball.xcor() > -350) and (ball.ball.ycor() < bat_a.bat.ycor() + 40 and ball.ball.ycor() > bat_a.bat.ycor() - 40):
            ball.ball.setx(-340)
            ball.ball.dx *= -1
