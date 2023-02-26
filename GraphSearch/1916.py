# BOJ 1916
# 최소비용 구하기
# 최단거리 -> Djikstra

import sys

import heapq
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M) : 
  a, b, cost = map(int, input().split())
  graph[a].append((b, cost))

start, end = map(int, input().split())

def dijkstra(start) : 
  d = [INF] * (N + 1)
  q = []
  heapq.heappush(q, (0, start))
  d[start] = 0

  while q : 
    dis, cur = heapq.heappop(q)
    if d[cur] < dis : 
      continue
    
    for v, cost in graph[cur] : 
      new_cost = dis + cost

      if d[v] > new_cost : 
        d[v] = new_cost
        heapq.heappush(q, (new_cost, v))
  return d

result = dijkstra(start)
print(result[end])
