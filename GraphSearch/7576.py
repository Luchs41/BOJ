# BOJ 7576
# 2차원 상자 안에 토마토가 저장되어 있다. 익은 토마토는 1, 익지 않은 토마토는 0, 빈 칸은 -1이다. 
# 익은 토마토는 가로세로 인접한 칸의 익지 않은 토마토를 하루 뒤 익게 만든다. 
# 모든 토마토가 익을 때 까지의 최소 날짜를 출력해야 한다. 입력의 첫 줄에는 상자의 크기 M, N이, 이후 줄에는 상자에 저장된 토마토의 정보가 주어진다. 

import sys

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
queue = deque()
def BFS() : 
    while queue : 
        x, y = queue.popleft()

        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if  0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0 : 
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))
                



M, N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(N) : 
    for j in range(M) : 
        if box[i][j] == 1 : 
            queue.append((i, j))

BFS()
for row in box : 
    for i in row : 
        if i == 0 : 
            print(-1)
            exit()
    ans = max(ans, max(row))
print(ans - 1)

