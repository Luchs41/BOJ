# BOJ 14940
# 쉬운 최단거리
# 지도의 어떤 지점 ~ 목표 지점(2) 까지의 거리를 구하는 문제
# {0, 1, 2} = {갈 수 없는 땅, 갈 수 있는 땅, 목표 지점}
# 가로m, 세로n, 2 <= n, m <= 1000
# 1000 * 1000 = 1,000,000
# 거리 : 원래 갈 수 없으면 0, 갈 수 있는 땅인데 못 가는거면 -1
# DP 해야하나?

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

target = (-1, -1)
for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      target = (i, j)

# target 까지의 거리를 담는 배열
dist = [[-1 for _ in range(m)] for _ in range(n)]
# 막힌 벽 미리 0으로 만들기
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      dist[i][j] = 0

# BFS 하면서 거리 재기
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visit = [[False for _ in range(m)] for _ in range(n)]
q = deque()
q.append(target)
dist[target[0]][target[1]] = 0

visit[target[0]][target[1]] = True
while q:
  cx, cy = q.popleft()
  visit[cx][cy] = True
  for i in range(4):
    x, y = cx + dx[i], cy + dy[i]
    # 유효한 좌표 확인
    if 0 <= x < n and 0 <= y < m and graph[x][y] == 1 and visit[x][y] == False:
      # 갈 수 있는 좌표면 거리계산 + 큐에넣기
      dist[x][y] = dist[cx][cy] + 1
      visit[x][y] = True
      q.append((x, y))

for line in dist:
  print(*line)