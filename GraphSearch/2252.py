# BOJ 2252
# 줄 세우기
# 위상 정렬 : in_degree -> 화살표가 꽂히는 갯수
# in_degree가 0인 노드들을 방문하면서 순서를 기록
# Cycle이 있으면 위상정렬 불가능

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for i in range(M) : 
  a, b = map(int, input().split())
  graph[a].append(b)
  in_degree[b] += 1

q = deque()
for i in range(1, N + 1) : 
  if in_degree[i] == 0 : 
    q.append(i)

result = []
while q : 
  cur = q.popleft()
  result.append(cur)
  for end in graph[cur] : 
    in_degree[end] -= 1
    if in_degree[end] == 0 : 
      q.append(end)
  
print(*result)