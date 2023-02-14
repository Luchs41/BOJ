# BOJ 7569
# 토마토 2.0
# 토마토를 3차원으로 저장. 
import sys
input = sys.stdin.readline
from collections import deque
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split())
box = []
q = deque()
for _ in range(H) : 
  temp = [list(map(int, input().split())) for i in range(N)]
  box.append(temp)

for i in range(H) : # z
  for j in range(N) : # y
    for k in range(M) : # x
      if box[i][j][k] == 1 : 
        q.append((i, j, k))
        

def BFS() : 
  while q : 
    x, y, z = q.popleft()
    for i in range(6) : 
      nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
      if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and box[nx][ny][nz] == 0: 
        #print(nz, ny, nx)
        box[nx][ny][nz] += box[x][y][z] + 1
        q.append((nx, ny, nz))

BFS()
result = 0
for i in box : 
  for j in i : 
    for k in j : 
      if k == 0 : 
        print(-1)
        exit(0)
    result = max(result, max(j))
print(result - 1)