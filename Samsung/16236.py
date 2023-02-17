# BOJ 16236
# 아기 상어
# 상어 가지고 탐색
# 정렬 시 lambda 함수로 key주는거 공부하기

import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


n = int(input())
graph = []
for i in range(n) :
  line = list(map(int, input().rstrip().split()))
  for j in range(n) :
    if line[j] == 9 :
      curx, cury = i, j
  graph.append(line)
graph[curx][cury] = 0


def BFS() : 
  global size
  
  q = deque()
  visit = [[False] * n for _ in range(n)]
  dist = [[0] * n for _ in range(n)]
  q.append((curx, cury))
  visit[curx][cury] = True
  fish = []
  while q : 
    x, y= q.popleft()
    for i in range(4) : 
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == False: 
        if graph[nx][ny] <= size : 
          q.append((nx, ny))
          visit[nx][ny] = True
          dist[nx][ny] = dist[x][y] + 1
          
          if graph[nx][ny] < size and graph[nx][ny] != 0 : 
            fish.append((nx, ny, dist[nx][ny]))
  
  return sorted(fish, key = lambda x : (-x[2], -x[0], -x[1]))

size = 2
stack = 0
total_time = 0
while 1 : 
  result = BFS()
  #print(result)
  if len(result) == 0 : 
    break
  graph[curx][cury] = 0
  curx, cury, time = result.pop()
  total_time += time
  graph[curx][cury] = 0
  
  stack += 1
  if stack == size : 
    size += 1
    stack = 0
print(total_time)