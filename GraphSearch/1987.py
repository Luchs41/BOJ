# BOJ 1987
# 알파벳
# 세로 R칸, 가로 C칸으로 된 보드. 좌측 상단(0, 0)에 말이 있다. 
# 말은 상하좌우 인접한 칸으로 이동 가능. 같은 알파벳이 적힌 칸을 두 번 지날 수 없다. 
# 최대 몇 칸을 지날 수 있는지 출력
# DFS로 해결, pypy3에서 통과..

import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
alpha = set()
alpha.add(board[0][0])
result = 0

def DFS(x, y, dist) : 
  global result
  result = max(dist, result)
  for i in range(4) : 
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < R and 0 <= ny < C  and board[nx][ny] not in alpha : 
      alpha.add(board[nx][ny])
      DFS(nx, ny, dist + 1)
      alpha.remove(board[nx][ny])
  return 0

DFS(0, 0, 1)
print(result)