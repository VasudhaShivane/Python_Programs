import math
def circle_area(r):
    area = math.pi * r* r
    return area


def mullti(a,b=0,*args):
    mul = a*b
    for d in args:
        mul = mul*d
    return mul 