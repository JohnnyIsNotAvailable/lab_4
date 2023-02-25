import math 
def radian(a):
    pi = 22/7
    radian = a * (pi / 180)
    return radian

def ctg(x): return math.cos(x)/math.sin(x)

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
angle_deg = 180 / n
deg = radian(angle_deg)
ans = n * l * l /4  * ctg(deg)

print("The area of the polygon is: ", f'{ans:.0f}')