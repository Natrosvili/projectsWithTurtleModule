from turtle import Turtle, Screen

player1 = Turtle()

player1.shape("classic")
player1.speed(8)
player1.penup()
player1.right(90)
player1.forward(190)
player1.left(90)
player1.pendown()

player1.begin_fill()
player1.pencolor("red")
player1.left(30)
player1.forward(200)
player1.left(50)
player1.forward(280)
player1.left(80)
player1.forward(230)
player1.left(40)
player1.forward(230)
player1.left(80)
player1.forward(280)
player1.fillcolor("red")
player1.end_fill()

player1.color("black")
player1.pencolor("white")
player1.penup()
player1.left(100)
player1.forward(60)
player1.left(48)
player1.pendown()
player1.begin_fill()
player1.forward(300)
player1.right(135)
player1.forward(300)
player1.right(113)
player1.forward(50)
player1.right(67)
player1.forward(97)
player1.left(67)
player1.forward(55)
player1.left(66)
player1.forward(98)
player1.fillcolor("white")
player1.end_fill()

player1.color("black")
player1.penup()
player1.left(184)
player1.forward(130)
player1.pendown()
player1.begin_fill()
player1.pencolor("red")
player1.left(4)
player1.forward(80)
player1.right(145)
player1.forward(82)
player1.fillcolor("red")
player1.end_fill()
player1.penup()
player1.home()

myScreen = Screen()
myScreen.exitonclick()