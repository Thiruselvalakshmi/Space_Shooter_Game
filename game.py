import turtle
import random

scr=turtle.Screen()
scr.title("Space Game")
scr.bgpic("D:\MY DETAILS (THIRU)\LMES\game4\Space.gif")
scr.setup(700,700)
scr.register_shape("D:\MY DETAILS (THIRU)\LMES\game4\Fighter.gif")
scr.tracer(0)

fighter=turtle.Turtle()
fighter.shape("D:\MY DETAILS (THIRU)\LMES\game4\Fighter.gif")
fighter.penup()
fighter.goto(0,-280)

bullet=turtle.Turtle()
bullet.shape("triangle")
bullet.setheading(90)
bullet.shapesize(0.25)
bullet.color("yellow")
bullet.penup()
bullet.goto(0,-265)
bullet.hideturtle()
bullet_state="ready"

enemy_count=8
enemy_speed=0.25
enemies=[]

for i in range(enemy_count):
    x=random.randint(-275,275)
    y=random.randint(150,280)
    enemy=turtle.Turtle()
    enemy.shape("turtle")
    enemy.setheading(270)
    enemy.color("green")
    enemy.penup()
    enemy.goto(x,y)
    enemies.append(enemy)

score = turtle.Turtle()
score.color("yellow")
score.shape("square")
score.penup()
score.goto(150,300)
score.write("Score : 0", font=("MV Boli",24,"bold"))
score.hideturtle()
pts = 0

scr.listen()

def fighter_right():
    x=fighter.xcor()
    x+=20
    if x>275:
        x=275
    fighter.setx(x)

def fighter_left():
    x=fighter.xcor()
    x-=20
    if x<-275:
        x=-275
    fighter.setx(x)

def shoot():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(fighter.xcor(),fighter.ycor())
        bullet.showturtle()

scr.onkeypress(fighter_right,"Right")
scr.onkeypress(fighter_left,"Left")
scr.onkeypress(shoot,"space")

while True:
    scr.update()
    for enemy in enemies:
        x=enemy.xcor()
        y=enemy.ycor()
        pos=0
        x=enemy_speed+x
        enemy.setx(x)
        if x>275:
            y-=20
            enemy.sety(y)
            enemy_speed*=-1
        if x<-275:
            y-=20
            enemy.sety(y)
            enemy_speed*=-1
        if enemy.distance(bullet) < 15:
            x=random.randint(-275,275)
            y=random.randint(150,280)
            enemy.goto(x,y)
            bullet.hideturtle()
            bullet.goto(1000,1000)
            bullet_state = "ready"
            pts+=10
            score.clear()
            score.write("Score : {}".format(pts), font=("MV Boli",24,"bold"))
            
        if enemy.ycor() < -280:
            print("Game over")
            print("Your score : ",pts)
            exit()

    if bullet.ycor() >= 300:
        bullet.hideturtle()
        bullet.goto(1000,1000)
        bullet_state = "ready"

    if bullet_state == "fire":
        y = bullet.ycor()
        bullet.sety(y+20)
        
turtle.done()