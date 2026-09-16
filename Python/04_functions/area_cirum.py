import math

def area_curm(radius):
    area = math.floor(math.pi * radius ** 2)
    circumfarance = math.floor(2 * math.pi * radius)
    return area, circumfarance

a , c = area_curm(3)
print("area:", a , "circumfarance: ", c)