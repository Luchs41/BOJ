# BOJ 1005
# ACM Craft
# 특정 건물을 짓기 위한 최소시간 구하기
# 위상정렬, DP
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T) : 
  N, K = map(int, input().split())
  D = [0] + list(map(int, input().split()))
  graph = [[] for _ in range(N + 1)]
  in_degree = [0 for _ in range(N + 1)]
  cost = [0 for _ in range(N + 1)]
  
  for _ in range(K) : 
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1
  
  q = deque()
  for i in range(1, N+1) : 
    if in_degree[i] == 0 : 
      q.append(i)
      cost[i] = D[i]
  
  while q : 
    cur = q.popleft()
    for i in graph[cur] : 
      in_degree[i] -= 1
      cost[i] = max(cost[cur] + D[i], cost[i])
      if in_degree[i] == 0 : 
        q.append(i)
  
  target = int(input())
  print(cost[target])
