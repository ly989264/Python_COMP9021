from turtle import *

def draw_six(colour):
    color(colour)
    for i in range(0,3):
        each()
        left(ang)

def each():
    pendown()
    forward(distance)
    penup()
    forward(distance)
    pendown()
    forward(distance)
    penup()

distance=30
ang=120
penup()
forward(-1.5*distance)
pendown()
while True:
    draw_six('red')
    penup()
    left(270)
    backward(1.73*distance)
    pendown()
    left(30)
    draw_six('blue')
    penup()
    left(270)
    backward(1.73 * distance)
    pendown()
    left(30)