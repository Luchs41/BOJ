# BOJ 2178
# 미로의 첫째 칸에서 마지막 칸으로 이동하는 최단경로의 길이를 출력하는 문제. (항상 도착위치로 이동할 수 있는 경우만 주어진다. )
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) : 
    queue = deque()
    queue.append((x, y))
    while queue : 
        x, y = queue.popleft()
        
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로의 최대 범위 내인지 확인
            if nx < 0 or nx >= N or ny < 0 or ny >= M : 
                continue

            if maze[nx][ny] == 0 : 
                continue

            if maze[nx][ny] == 1 : 
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[N - 1][M - 1]

N, M = map(int, input().split())
maze = []
for _ in range(N) : 
    maze.append(list(map(int, input())))
    
print(bfs(0, 0))