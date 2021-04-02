import turtle
import random
import time

delay = 0.1
score=0

highestscore=0

# snakebodies
bodies=[]

#create a screen  | canvas

s=turtle.Screen()
s.title("Snake Game")
s.bgcolor('silver')
s.setup(width=600,height=600)

#create snake head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"


#snake food
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('yellow')
food.fillcolor('green')
food.penup()
food.ht()
food.goto(0,200)
food.st()

#score board
sb=turtle.Turtle()
sb.shape('circle')
sb.fillcolor('black')
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score: 0  |  Highest Score: 0")


def moveup():
    if head.direction!="down":
       head.direction="up"
def movedown():
    if head.direction!="up":
       head.direction="down"

def moveright():
    if head.direction!="left":
       head.direction="right"
def moveleft():
    if head.direction!="right":
       head.direction="left"

def movestop():
    head.direction="stop"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)



# event handling - key mappings

s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")



#main loop

while True:
    s.update()  #to update screen

    #check collision with border
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)


    #collision with food
    if head.distance(food)<20:
        #moove the food to new random place
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #incease length of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape('circle')
        body.color('red')
        body.fillcolor('black')
        bodies.append(body) #append body

        #increse the score
        score+=10

        #change delay
        delay-=0.001

        #update the highest score
        if score>highestscore:
            highestscore=score
        sb.clear()
        sb.write("Score: {}  Highest Score: {}".format(score,highestscore)) ###### format function

        #move the snake bodies
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)

    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()

    #check collision with snake body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()

            score=0
            delay=0.1
            #update Score board
            sb.clear()
            sb.write("Score:  {}   Highest Score: {} ".format(score,highestscore))
    time.sleep(delay)
s.mainloop()
       
           
# code ended        
                 
        
        