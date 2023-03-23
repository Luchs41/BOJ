# BOJ 14003
# 가장 긴 증가하는 부분 수열 5
# 길이와 해당 수열을 동시에 출력
# DP의 과정을 기억하는 작업이 필요하겠다..

import bisect
import sys
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))
mem = [0] * (n + 1)
dp = [-float('inf')]

for i in range(1, n + 1) : 
  if a[i] > dp[-1] : 
    dp.append(a[i])
    mem[i] = len(dp) - 1
  else : 
    mem[i] = bisect.bisect_left(dp, a[i])
    dp[mem[i]] = a[i]
print(len(dp) - 1)

idx = max(mem) + 1
result = list()
for i in range(n, 0, -1) : 
  if mem[i] == idx - 1 : 
    result.append(a[i])
    idx = mem[i]

print(*result[::-1])