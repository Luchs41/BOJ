# BOJ 4963
# 섬의 개수
# 1은 땅, 0은 바다일 때, 섬의 개수를 구하여라
# 두 타일이 같은 섬 -> 가로, 세로, 대각선으로 연결되어 있어야 함
# BFS -> 1인 땅을 기준으로 시작, 연결된 땅들을 체크하고 0으로 바꾸어줌


from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y) : 
  dx = [1, -1, 0, 0, 1, -1, 1, -1]
  dy = [0, 0, -1, 1, -1, 1, 1, -1]
  field[x][y] = 0
  q = deque()
  q.append([x, y])
  while q : 
    a, b = q.popleft()
    for i in range(8) : 
      nx = a + dx[i]
      ny = b + dy[i]
      if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1 : 
        field[nx][ny] = 0
        q.append([nx, ny])

while 1 : 
  w, h = map(int, input().split())
  if w == h == 0 : 
    break
  field = []
  island = 0
  for _ in range(h) : 
    field.append(list(map(int, input().split())))
  
  for i in range(h) : 
    for j in range(w) : 
      if field[i][j] == 1 : 
        bfs(i, j)
        island += 1
  
  print(island)