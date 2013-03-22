import math

def distance(x1,y1,x2,y2) :
  return math.sqrt((x2-x1)**2 + (y2-y1)**2)

x1 = input('x1 : ')
y1 = input('y1 : ')
x2 = input('x2 : ')
y2 = input('y2 : ')

print distance(x1,y1,x2,y2)