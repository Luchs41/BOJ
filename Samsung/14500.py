# BOJ 14500
# 테트로미노
# 정사각형 4개를 이어 붙인 도형(테트로미노)를 NXM 종이 위에 놓는다. 
# 테트로미노가 놓인 칸에 쓰여있는 수들의 합의 최댓값 출력
# 2차원 배열 초기화 시 주의하자. -> * 쓰지말고 for로 만들기
N, M = map(int, input().split())
board = []
for _ in range(N) : 
  board.append(list(map(int, input().split())))


# board = [list(map(int,input().split())) for _ in range(N)]
# visited = [[False] * M] * N
visited = [[False] * M for _ in range(N)]


# for line in board : 
#   print(line)
# print('---')
# for line in visited : 
#   print(line)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


Max = 0

def DFS(x, y, length, total) : 
  global Max
  if length == 4 : 
    Max = max(Max, total)
    return
  
  for i in range(4) : 
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] : 
      visited[nx][ny] = True
      DFS(nx, ny, length + 1, total + board[nx][ny])
      visited[nx][ny] = False

def ㅗ(x, y) : 
  global Max
  for i in range(4) : 
    temp = board[x][y]
    for j in range(3) : 
      k = (i + j) % 4
      nx = x + dx[k]
      ny = y + dy[k]

      if not (0 <= nx < N and 0 <= ny < M) : 
        temp = 0
        break
      temp += board[nx][ny]
    
    Max = max(Max, temp)


for i in range(N) : 
  for j in range(M) : 
    visited[i][j] = True
    DFS(i, j, 1, board[i][j])
    visited[i][j] = False
    
    ㅗ(i, j)


print(Max)
