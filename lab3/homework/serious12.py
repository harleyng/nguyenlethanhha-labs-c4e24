from serious11 import is_inside

a = int(input("given point on x-axis: "))
b = int(input("given point on y-axis: "))
x = int(input("rectangle lies on x-axis: "))
y = int(input("rectangle lies on y-axis: "))
width = int(input("rectangle's width: "))
height = int(input("rectangle's height: "))

point = [a, b]
rectangle = [x, y, width, height]

is_inside(point, rectangle)