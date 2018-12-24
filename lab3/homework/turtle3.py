from turtle import *

def draw_square(length, colour):
    color(colour)
    
    for _ in range(4):
        forward(length)
        left(90)