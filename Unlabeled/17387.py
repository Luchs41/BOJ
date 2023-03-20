# BOJ 17387
# 선분 교차 2
# 2차원 위의 두 선분이 교차하는지 구해보자. 끝 점이 만나도 교차하는 것으로 친다. 

import sys
from collections import Counter

input = sys.stdin.readline

class Point : 
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y

class Line : 
  def __init__(self, p1: Point, p2: Point) -> None:
    self.p1 = p1
    self.p2 = p2

def direction(a: Point, b: Point, c: Point) : 
  dxab = b.x - a.x
  dxac = c.x - a.x
  dyab = b.y - a.y
  dyac = c.y - a.y

  if dxab * dyac < dyab * dxac : 
    dir = 1
  elif dxab * dyac > dyab * dxac : 
    dir = -1
  else : 
    if dxab == 0 and dyab == 0 : 
      dir = 0
    if dxab * dxac < 0 or dyab * dyac < 0 : 
      dir = -1
    elif dxab * dxab + dyab * dyab >= dxac * dxac + dyac * dyac : 
      dir = 0
    else : 
      dir = 1
  return dir

def isCrossed(l1: Line, l2: Line) : 
  if direction(l1.p1, l1.p2, l2.p1) * direction(l1.p1, l1.p2, l2.p2) <= 0 and \
      direction(l2.p1, l2.p2, l1.p1) * direction(l2.p1, l2.p2, l1.p2) <= 0 : 
    return True
  return False

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

line1 = Line(Point(x1, y1), Point(x2, y2))
line2 = Line(Point(x3, y3), Point(x4, y4))

if isCrossed(line1, line2) : 
  print(1)
else : 
  print(0)