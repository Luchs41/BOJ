# BOJ 11660
# 구간 합 구하기 5
# N X N의 표에서 (x1, y1) ~ (x2, y2)까지의 합을 구하는 프로그램을 작성
# 구간합 -> 메모이제이션(DP)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N) : 
  arr.append(list(map(int, input().split())))

sum_arr = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1) : 
  for j in range(1, N + 1) : 
    sum_arr[i][j] = sum_arr[i][j - 1] + sum_arr[i - 1][j] - sum_arr[i - 1][j - 1] + arr[i - 1][j - 1]

for _ in range(M) : 
  x1, y1, x2, y2 = map(int, input().split())

  print(sum_arr[x2][y2] - sum_arr[x1 - 1][y2] - sum_arr[x2][y1 - 1] + sum_arr[x1 - 1][y1 - 1])
