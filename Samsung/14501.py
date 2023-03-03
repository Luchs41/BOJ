# BOJ 14501
# 퇴사
# DP로 해결
# 안됐던 이유 -> 마지막 날을 딱 맞춰서 끝낸 경우, N + 1에 최댓값이 저장되고
# 그게 아니면 N에 최댓값이 저장됨
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
consult = list()
consult.append((-1, -1))
for i in range(N) : 
  day, pay = map(int, input().split())
  consult.append((day, pay))

dp = [0] * 22

for i in range(1, N + 1) : 
  
  dp[i] = max(dp[i - 1], dp[i])
  dp[i + consult[i][0]] = max(dp[i + consult[i][0]], dp[i] + consult[i][1])

print(max(dp[N], dp[N+1])) # dp[:N + 2]에서 수정