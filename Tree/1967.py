# BOJ 1967
# 트리의 지름 구하기
# 1167번으로 날먹
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1) : 
  v = list(map(int, input().split()))
  graph[v[0]].append((v[1], v[2]))
  graph[v[1]].append((v[0], v[2]))

def BFS(v) : 
  q = deque()
  q.append(v)
  visit = [-1] * (n + 1)
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

# print(graph)
dist, vertex = BFS(1)
# print(dist, vertex)
dist, vertex = BFS(vertex)
# print(dist, vertex)
print(dist)