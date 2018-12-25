from turtle import *

def draw_star(x, y, length):
    penup()
    goto(x, y)
    pendown()
    
    for _ in range(5):
        forward(length)
        right(144)