# BOJ 11724
# 연결 요소(Connected Component)의 개수를 구해라
# 정점의 개수 N, 간선의 개수 M
# 이후 M개의 줄에 간선의 양 끝점 u와 v

import sys
from collections import deque
input = sys.stdin.readline

def BFS(v) : 
  q = deque()
  visit[v] = 1
  q.append(v)
  while q : 
    cur = q.popleft()
    for i in range(1, N + 1) : 
      if graph[cur][i] == 1 and visit[i] == 0 : 
        
        visit[i] = 1
        q.append(i)


N, M = map(int, input().split())
graph = [[-1] * (N + 1) for _ in range(N + 1)]
visit = [0] * (N + 1)
for _ in range(M) : 
  u, v = map(int, input().split())
  graph[u][v] = 1
  graph[v][u] = 1

result = 0

for i in range(1, N + 1) : 
  if visit[i] == 0 : 
    BFS(i)
    result += 1
    
print(result)
