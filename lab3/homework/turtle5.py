from turtle import *

def draw_star(x, y, length):
    goto(x, y)
    for _ in range(5):
        forward(length)
        right(144)