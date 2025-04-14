def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b==0:
        raise ValueError("numbers cannot be divided by 0")
    return a/b
