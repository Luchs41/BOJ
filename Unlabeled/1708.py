# BOJ 1708
# 볼록껍질
# N개의 점이 주어졌을 때 Convex Hull을 이루는 점의 개수를 구하시오

import sys

def diff(p1, p2) : 
  return p2[0] - p1[0], p2[1] - p1[1]

def ccw(p1, p2, p3) : 
  v, u = diff(p1, p2), diff(p2, p3)
  if v[0] * u[1] > v[1] * u[0] : 
    return True
  else : 
    return False

def convexHull(pos) : 
  convex = []
  for p3 in pos : 
    while len(convex) >= 2 : 
      p1, p2 = convex[-2], convex[-1]
      if ccw(p1, p2, p3) : 
        break
      convex.pop()
    convex.append(p3)
  
  return len(convex)

input = sys.stdin.readline
n = int(input())
result = -2
positions = []
for _ in range(n) : 
  positions.append(list(map(int, input().split())))

positions = sorted(positions, key = lambda pos:(pos[0], pos[1]))
result += convexHull(positions)

positions.reverse()
result += convexHull(positions)
print(result)