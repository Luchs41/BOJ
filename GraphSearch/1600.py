# BOJ 1600
# 말이 되고픈 원숭이
# 왼쪽 위에서 오른쪽 아래까지 내려가기
# 단 K번만큼 체스의 나이트처럼 움직일 수 있음
# 시작점에서 도착점까지 가는 최소 동작수 출력
# 1은 장애물, 0은 이동가능

from collections import deque
import sys
input = sys.stdin.readline

dn = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 일반 움직임
dk = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)] # 말의 움직임

k = int(input())
w, h = map(int, input().split())
board = []
for _ in range(h) : 
  board.append(list(map(int, input().split())))


def bfs() : 
  q = deque()
  visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
  q.append((0, 0, 0))
  visited[0][0][0] = 1
  while q : 
    cx, cy, jump = q.popleft()
    if cx == h - 1 and cy == w - 1 : 
      return visited[cx][cy][jump] - 1
    
    for (a, b) in dn : 
      dx, dy = cx + a, cy + b
      if 0 <= dx < h and 0 <= dy < w and visited[dx][dy][jump] == 0 and board[dx][dy] == 0 : 
        visited[dx][dy][jump] = visited[cx][cy][jump] + 1
        q.append((dx, dy, jump))
    
    if jump < k : 
      for (a, b) in dk : 
        dx, dy = cx + a, cy + b
        if 0 <= dx < h and 0 <= dy < w and visited[dx][dy][jump + 1] == 0 and board[dx][dy] == 0 : 
          visited[dx][dy][jump + 1] = visited[cx][cy][jump] + 1
          q.append((dx, dy, jump + 1))
  
  return -1



    

print(bfs())

