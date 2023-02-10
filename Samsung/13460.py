# BOJ 13460
# 구슬 탈출

from collections import deque

N, M = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = []
rx, ry = 0, 0
bx, by = 0, 0
for i in range(N) : 
  board.append(list(input()))
  for j in range(M) : 
    if board[i][j] == "R" : 
      rx, ry = i, j
    elif board[i][j] == "B" : 
      bx, by = i, j

def BFS(rx, ry, bx, by) : 
  q = deque()
  q.append((rx, ry, bx, by))
  visit = []
  visit.append((rx, ry, bx, by))
  count = 0
  while q : 
    for _ in range(len(q)) : 
      rx, ry, bx, by = q.popleft()
      if count > 10 : 
        print(-1)
        return
      if board[rx][ry] == 'O' : 
        print(count)
        return
      for i in range(4) : 
        nrx, nry = rx, ry
        while True : 
          nrx += dx[i]
          nry += dy[i]
          if board[nrx][nry] == '#' : 
            nrx -= dx[i]
            nry -= dy[i]
            break
          if board[nrx][nry] == 'O' : 
            break
        nbx, nby = bx, by
        while True : 
          nbx += dx[i]
          nby += dy[i]
          if board[nbx][nby] == '#' : 
            nbx -= dx[i]
            nby -= dy[i]
            break
          if board[nbx][nby] == 'O' : 
            break
        if board[nbx][nby] == 'O' : 
          continue
        if nrx == nbx and nry == nby : 
          if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by) : 
            nrx -= dx[i]
            nry -= dy[i]
          else : 
            nbx -= dx[i]
            nby -= dy[i]
        if (nrx, nry, nbx, nby) not in visit : 
          q.append((nrx, nry, nbx, nby))
          visit.append((nrx, nry, nbx, nby))
    count += 1
  print(-1)
BFS(rx, ry, bx, by)



