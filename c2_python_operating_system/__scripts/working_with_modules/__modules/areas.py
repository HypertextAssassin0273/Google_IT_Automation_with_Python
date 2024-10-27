import math

def triangle(base, height):
    return base * height / 2

def square(side):
    return side ** 2

def rectangle(width, height):
    return width * height

def circle(radius):
    return math.pi * radius ** 2

def doughnut(outer_radius, inner_radius):
    return circle(outer_radius) - circle(inner_radius)

# note: a 'module' file only contains non-executable statements & definitions
