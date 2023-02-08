# BOJ 1167
# 트리의 지름 : 트리에서 임의의 두 점 사이 거리 중 가장 긴 것
# 지름을 구하는 법 : 임의의 정점에서 가장 멀리 떨어진 정점 x를 구함
# x에서 가장 멀리 떨어진 정점 y까지의 거리 == 트리의 지름
import sys
input = sys.stdin.readline
from collections import deque

def BFS(v) : 
  q = deque()
  q.append(v)
  visit = [-1] * (V + 1)
  dist, vertex = 0, 0
  visit[v] = 0
  while q : 
    cur = q.popleft()
    for e, w in graph[cur] : 
      if visit[e] == -1 : 
        visit[e] = visit[cur] + w
        q.append(e)
        if dist < visit[e] : 
          dist = visit[e]
          vertex = e
  return dist, vertex

V = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(V) : 
  v = list(map(int, input().split()))
  for i in range(1, len(v) - 2, 2) : 
    graph[v[0]].append((v[i], v[i + 1]))

dist, vertex = BFS(1)
dist, vertex = BFS(vertex)
print(dist)