import math as mt
def distance(x1, y1, x2, y2):
 return mt.sqrt((x1 - x2)**2 + (y1 - y2)**2)
x2 = float(input())
x1 = float(input())
y2 = float(input())
y1 = float(input())
print(distance(x1, y1, x2, y2))