from turtle import *
import turtle
turtle.bgcolor('black')
turtle.pencolor('red')
turtle.hideturtle()
turtle.speed()
#curve01
def curve01(a,d):
    for i in range(d):
        turtle.right(a)
        turtle.forward(1)
        

#curve02
def curve02(a,d):
    for i in range(d):
        turtle.left(a)
        turtle.forward(1)
        

#making left face
turtle.fillcolor('red')
turtle.begin_fill()
turtle.speed()
turtle.pendown()
turtle.left(90)
curve01(5,20)
turtle.left(175)
turtle.forward(50)
turtle.left(25)
turtle.forward(28)
turtle.right(160)
turtle.forward(170)
curve02(0.2,65)
turtle.right(60)
curve01(0.1,140)
curve01(0.5,50)
turtle.left(180)
curve02(0.2,150)
curve02(0.1,95)
turtle.left(127)
turtle.forward(5)
curve01(2,20)
turtle.right(30)
turtle.forward(90)
turtle.right(7)
turtle.forward(75)
turtle.right(160)
turtle.forward(100)
curve02(0.1,105)
turtle.right(70)
curve01(0.2,200)
curve01(0.3,70)
turtle.left(175)
curve02(0.2,150)
curve02(0.3,150)
turtle.forward(20)
turtle.left(65)
curve01(0.1,120)
curve01(0.010,105)
turtle.right(10)
curve01(0.2,110)
turtle.right(60)
curve01(0.3,138)
turtle.right(30)
curve01(0.2,160)
turtle.left(150)
curve02(0.2,100)
curve02(0.1,150)
turtle.forward(70)
curve02(0.4,40)
turtle.left(160)
curve01(0.1,60)
turtle.left(7)
curve01(0.1,120)
curve01(0.2,30)
turtle.forward(20)
turtle.right(140)
curve02(0.2,40)
turtle.right(50)
curve02(0.2,70)
turtle.right(8)
curve02(0.1,70)
curve02(0.5,50)
turtle.left(153)
curve01(0.1,170)
turtle.right(81)
curve02(0.2,20)
turtle.right(3)
curve02(0.1,62)
turtle.right(153) #..
curve01(0.1,63) 
turtle.left(50)
curve02(0.1,175)
turtle.left(60)
turtle.forward(7)
turtle.end_fill()


#going to replicate
turtle.left(92.15)
turtle.penup()
turtle.forward(417)
turtle.pendown()

turtle.fillcolor('red')
turtle.begin_fill()
#right face 
turtle.right(90)
curve02(5,20)
turtle.right(175)
turtle.forward(50)
turtle.right(25)
turtle.forward(28)
turtle.left(160)
turtle.forward(170)
curve01(0.2,65)
turtle.left(60)
curve02(0.1,140)
curve02(0.5,50)
turtle.right(180)
curve01(0.2,150)
curve01(0.1,95)
turtle.right(127)
turtle.forward(5)
curve02(2,20)
turtle.left(30)
turtle.forward(90)
turtle.left(7)
turtle.forward(75)
turtle.left(160)
turtle.forward(100)
curve01(0.1,105)
turtle.left(70)
curve02(0.2,200)
curve02(0.3,70)
turtle.right(175)
curve01(0.2,150)
curve01(0.3,150)
turtle.forward(20)
turtle.right(65)
curve02(0.1,120)
curve02(0.010,105)
turtle.left(10)
curve02(0.2,110)
turtle.left(60)
curve02(0.3,138)
turtle.left(30)
curve02(0.2,160)
turtle.right(150)
curve01(0.2,100)
curve01(0.1,150)
turtle.forward(70)
curve01(0.4,40)
turtle.right(160)
curve02(0.1,60)
turtle.right(7)
curve02(0.1,120)
curve02(0.2,30)
turtle.forward(20)
turtle.left(140)
curve01(0.2,40)
turtle.left(50)
curve01(0.2,70)
turtle.left(8)
curve01(0.1,70)
curve01(0.5,50)
turtle.right(153)
curve02(0.1,170)
turtle.left(81)
curve01(0.2,20)
turtle.left(3)
curve01(0.1,62)
turtle.left(153) #..
curve02(0.1,63) 
turtle.right(50)
curve01(0.1,100)  #0.1
turtle.forward(75)
turtle.right(75)
turtle.forward(2)
turtle.end_fill()
turtle.done() 