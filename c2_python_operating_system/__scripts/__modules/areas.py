import math

def triangle(base, height):
    return base * height / 2

def rectangle(width, height):
    return width * height

def circle(radius):
    return math.pi * radius ** 2

def doughnut(outer_radius, inner_radius):
    return circle(outer_radius) - circle(inner_radius)

# notes:
# 1)  this is a file to be used as a module
# 2)  such files do not contain any executable code (i.e. only definitions, classes, functions, etc)
