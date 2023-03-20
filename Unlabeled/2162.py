# BOJ 2162
# 선분 그룹
# N개의 선분들이 이루는 그룹의 크기를 출력, 가장 큰 그룹에 속한 선분의 개수도 출력

import sys
input = sys.stdin.readline
from collections import Counter
N = int(input())
line = []
parent = [i for i in range(N)]
for i in range(N) : 
  line.append(list(map(int, input().split())))

def ccw(x1, y1, x2, y2, x3, y3) : 
  return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def isCrossed(line1, line2) : 
  x1, y1, x2, y2 = line1
  x3, y3, x4, y4 = line2

  mx1, my1 = min(x1, x2), min(y1, y2)
  mx2, my2 = max(x1, x2), max(y1, y2)
  mx3, my3 = min(x3, x4), min(y3, y4)
  mx4, my4 = max(x3, x4), max(y3, y4)

  ccw123 = ccw(x1, y1, x2, y2, x3, y3)
  ccw124 = ccw(x1, y1, x2, y2, x4, y4)
  ccw341 = ccw(x3, y3, x4, y4, x1, y1)
  ccw342 = ccw(x3, y3, x4, y4, x2, y2)

  if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
    if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
      return True
  else:
    if ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:
      return True

  return False

def find(parent, x) : 
  if parent[x] != x : 
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent, a, b) : 
  a = find(parent, a)
  b = find(parent, b)
  if a < b : 
    parent[b] = a
  else : 
    parent[a] = b

for i in range(N - 1) : 
  for j in range(i + 1, N) : 
    if isCrossed(line[i], line[j]) : 
      union(parent, i, j)

cnt = 0
cnt_ = [0] * N
for i in range(N) : 
  if i == parent[i] : 
    cnt += 1
  cnt_[find(parent, i)] += 1

print(cnt)
print(max(cnt_))
