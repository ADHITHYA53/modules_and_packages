import math
def sqrt(a):
    if a<0:
        raise ValueError("square root for negative numbers are imaginary.")
    return math.sqrt(a)
def power(a,b):
    return math.pow(a,b)
def log(a,b=10):
    #b=base
    if a<=0:
        raise ValueError("logarithm for non positive numbers are not available.")
    return math.log(a,b)
def sine(a):
    #a=angle
    return math.sin(math.radians(a))
def cosine(a):
    return math.cos(math.radians(a))
def tangent(a):
    return math.tan(math.radians(a))

