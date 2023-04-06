# BOJ 2239
# 스도쿠
# 주어진 스도쿠를 완성해라. 0은 아직 안채워진 부분
# 답이 여러개라면 사전식으로 앞서는 것을 출력
# 백트래킹 dfs로 해결

import sys
input = sys.stdin.readline

sudoku = [list(map(int,list(input().rstrip()))) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def dfs(n) : 
  if n == len(zeros) : 
    for i in sudoku :
      print(*i, sep="")
    sys.exit()
  
  x, y = zeros[n]
  mid_x, mid_y = x // 3, y // 3
  lefts = list(range(1, 10))

  for i in range(mid_x * 3, (mid_x + 1) * 3) : 
    for j in range(mid_y * 3, (mid_y + 1) * 3) : 
      if sudoku[i][j] in lefts : 
        lefts.remove(sudoku[i][j])
  
  for i in range(9) : 
    if sudoku[x][i] in lefts : 
      lefts.remove(sudoku[x][i])
    
    if sudoku[i][y] in lefts : 
      lefts.remove(sudoku[i][y])
  
  for left in lefts : 
    sudoku[x][y] = left
    dfs(n + 1)
  sudoku[x][y] = 0

dfs(0)