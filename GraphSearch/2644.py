# BOJ 2644
# 촌수 계산
# 첫 줄 : 전체 사람 수 n / 둘째 줄 : 촌수를 계산해야 하는 서로 다른 두 사람 / 셋째 줄 : 부모 자식들 간의 관계의 개수 m / 이후 : 고나계를 나타내는 두 번호
# x, y -> x는 y의 부모

from collections import deque

def bfs(a, b) : 
  q = deque()
  visited = [0] * (n + 1)
  q.append((a, 0))
  visited[a] = 1
  
  while q : 
    curPerson, curCount = q.popleft()
    visited[curPerson] = 1
    if curPerson == b : 
      return curCount
    for i in range(1, n + 1) : 
      if visited[i] == 0 and graph[curPerson][i] == 1 : 
        q.append((i, curCount + 1))
  
  return -1

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[0] * (n+1) for _ in range(n + 1)]

for _ in range(m) : 
  x, y = map(int, input().split())
  graph[x][y] = 1
  graph[y][x] = 1

print(bfs(a, b))

