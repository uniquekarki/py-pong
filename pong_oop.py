import turtle
from functools import partial

class Bat(turtle.Turtle):
    def __init__(self,side):
        super().__init__()
        self.bat_init(side)

    def bat_init(self, side):
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if side == 'a':
            self.goto(-350,0)
        else:
            self.goto(350,0)

    def bat_move(self,input):
        y = self.ycor()
        if input == 'a':
            y+=20
        elif input == 'b':
            y-=20
        else:
            pass
        self.sety(y)

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.ballinit()
        self.count_a = 0
        self.count_b = 0
        self.pen = turtle.Turtle()
        self.display_score()

    def ballinit(self):
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.dx = 0.06
        self.dy = 0.06

    def display_score(self):
        
        self.pen.speed(0)
        self.pen.color('white')
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0,260)
        self.pen.clear()
        self.pen.write('Player 1 : {}  |  Player 2 : {}'.format(self.count_a,self.count_b), align = 'center', font = ("Courier", 24, "normal"))


    def move_ball(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        if self.ycor() > 290:
            self.sety(290)
            self.dy *= -1

        if self.ycor() < -290:
            self.sety(-290)
            self.dy *= -1
        
        if self.xcor() > 390:
            self.goto(0,0)
            self.dx *= -1
            self.count_a +=1
            self.display_score()
            
        if self.xcor() < -390:
            self.goto(0,0)
            self.dx *= -1
            self.count_b +=1
            self.display_score()

if __name__ == '__main__':
    wn = turtle.Screen()
    wn.title("Ping Pong By Nick")
    wn.bgcolor("black")
    wn.setup(width = 800, height= 600)
    wn.tracer(0)

    bat_a = Bat("a")
    bat_b = Bat("b")
    ball = Ball()

    wn.listen()
    wn.onkey(partial(bat_a.bat_move, 'a'),'w')
    wn.onkey(partial(bat_a.bat_move, 'b'),'s')
    wn.onkey(partial(bat_b.bat_move, 'a'),'Up')
    wn.onkey(partial(bat_b.bat_move, 'b'),'Down')

    while True:
        wn.update()

        ball.move_ball()

        # Bat and Ball Collision
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bat_b.ycor() + 40 and ball.ycor() > bat_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bat_a.ycor() + 40 and ball.ycor() > bat_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
