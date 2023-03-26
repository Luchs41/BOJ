# BOJ 1197
# 최소 스패닝 트리(MST)
# 가중치를 출력한다. 
# Kruskal 크루스칼
# 깝치지 말고 union-find 할 것. 
import sys
input = sys.stdin.readline
from collections import deque

def find(x) : 
  if x == parent[x] : 
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y) : 
  x = find(x)
  y = find(y)

  if x < y : 
    parent[y] = x
  else : 
    parent[x] = y



V, E = map(int, input().split())
edge = list()
for _ in range(E) : 
  edge.append(list(map(int, input().split())))
edge = sorted(edge, key=lambda x : (x[2]))

parent = [i for i in range(V + 1)]

weightSum = 0
for v1, v2, weight in edge : 
  if find(v1) != find(v2) : 
    union(v1, v2)
    weightSum += weight


print(weightSum)
