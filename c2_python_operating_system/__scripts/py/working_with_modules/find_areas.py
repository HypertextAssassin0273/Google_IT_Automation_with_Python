#!/usr/bin/env python3

from __modules import areas

print("area of triangle:", areas.triangle(10, 5))

print("area of square:", areas.square(5))
print("area of rectangle:", areas.rectangle(10, 5))

print(f"area of circle: {areas.circle(4):.2f}")
print(f"area of doughnut: {areas.doughnut(8, 4):.2f}")
