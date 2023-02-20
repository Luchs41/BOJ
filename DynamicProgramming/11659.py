# BOJ 11659
# 구간 합 구하기
# 1~K까지 더한거 저장
# i~j까지의 합 = sum[j] - sum[i]

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
Sum = [0]
for i in range(1, N + 1) : 
  Sum.append(Sum[i - 1] + numbers[i - 1])

for _ in range(M) : 
  start, end = map(int, input().split())
  start -= 1
  print(Sum[end] - Sum[start])
    