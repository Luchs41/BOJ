# BOJ 1238
# N개의 마을 각각에 한 명의 학생이 산다
# 이 중 하나의 마을(X번 마을)에 모여서 파티를 한다. 마을 사이에는 M개의 도로가 존재
# 도로는 단방향
# 최단경로 -> Dijkstra
# heap push 할때는 cost를 앞에 둬야 cost순으로 정렬되겠죠?

import sys
input = sys.stdin.readline
import heapq
inf = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m) : 
  a, b, t = map(int, input().split())
  graph[a].append((b, t))


def Dijkstra(start) : 
  q = []
  dist = [inf] * (n + 1)

  heapq.heappush(q, (0, start))
  dist[start] = 0
  
  while q : 
    dis, cur = heapq.heappop(q)

    if dist[cur] < dis : 
      continue

    for v, cost in graph[cur] : 
      new_cost = dis + cost

      if dist[v] > new_cost : 
        dist[v] = new_cost
        heapq.heappush(q, (new_cost, v))

  return dist

result = 0
home = Dijkstra(x)
for i in range(1, n + 1) : 
  party = Dijkstra(i)
  result = max(result, party[x] + home[i])

print(result)