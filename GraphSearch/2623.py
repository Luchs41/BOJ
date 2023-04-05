# BOJ 2623
# 음악프로그램
# N명의 가수가 출연해야 할 순서를 보조pd M명이 정해놨음
# 그거에 맞춰서 가능한 출연 순서를 출력해야 합니다
# 위상 정렬로 해결
# 2252랑 입력형식이 달랐다. 

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M) : 
  arr = list(map(int, input().split()))
  for i in range(1, arr[0]) : 
    a, b = arr[i], arr[i + 1]
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

if len(result) != N : 
  print(0)
else : 
  for num in result : 
    print(num)