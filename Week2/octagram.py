from turtle import *

angle=45
inside_length=100
inside_list=[]
blue_list=[]
red_list=[]
outside_list=[]

def set_position_of_insider():
    penup()
    for i in range(0,8):
        right(i*angle)
        forward(inside_length)
        inside_list.append(pos())
        home()
    pendown()
    return

def fill_insider(colour):
    pendown()
    color(colour)
    begin_fill()
    for i in range(0,8):
        goto(inside_list[i])
        if i==7:
            goto(inside_list[0])
            break
        goto(inside_list[i+1])
        home()
    end_fill()
    return

def set_position_of_blue():
    blue_angle=22.5
    blue_length=180
    penup()
    home()
    for i in range(0,4):
        actual_angle=blue_angle+i*90
        right(actual_angle)
        forward(blue_length)
        blue_list.append(pos())
        home()
    home()
    pendown()
    return

def set_position_of_red():
    red_angle=22.5*3
    red_length=180
    penup()
    home()
    for i in range(0,4):
        actual_angle=red_angle+i*90
        right(actual_angle)
        forward(red_length)
        red_list.append(pos())
        home()
    home()
    pendown()
    return

def merge_blue_and_red_list():
    for i in range(0,4):
        outside_list.append(blue_list[i])
        outside_list.append(red_list[i])
    return

def draw_outside(colour1='blue',colour2='red'):
    penup()
    for i in range(0,8):
        penup()
        if i%2:
            color(colour2)
        else:
            color(colour1)
        goto(outside_list[i])
        pendown()
        begin_fill()
        goto(inside_list[i])
        if i==7:
            goto(inside_list[0])
        else:
            goto(inside_list[i+1])
        goto(outside_list[i])
        end_fill()
    return

set_position_of_insider()
set_position_of_blue()
set_position_of_red()
merge_blue_and_red_list()
while True:
    fill_insider('yellow')
    draw_outside()
