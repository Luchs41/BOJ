# BOJ 1260
# 주어지는 정점, 간선, 시작점에 대해서 DFS와 BFS를 수행하여 방문한 정점을 순서대로 출력. 
# 
import sys
from collections import deque
def bfs(v) : 
  queue = deque()
  queue.append(v)
  visit_bfs[v] = 1
  while queue : 
    p = queue.popleft()
    print(p, end = " ")
    for i in range(1, n + 1) : 
      if visit_bfs[i] == 0 and graph[p][i] == 1 : 
        queue.append(i)
        visit_bfs[i] = 1

def dfs(v) : 
  visit_dfs[v] = 1
  print(v, end=" ")
  for i in range(1, n + 1) : 
    if visit_dfs[i] == 0 and graph[v][i] == 1 : 
      dfs(i)

n, m, v = map(int, sys.stdin.readline().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m) : 
  a, b = map(int, sys.stdin.readline().split())
  graph[a][b] = 1
  graph[b][a] = 1
visit_dfs = [0] * (n + 1)
visit_bfs = [0] * (n + 1)

dfs(v)
print()
bfs(v)
print()