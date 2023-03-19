# BOJ 10942
# N개의 자연수 중, S~E번째 까지가 펠린드롬인지 아닌지 출력
# DP로 해결
import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

dp = [[False] * (N) for _ in range(N)]
for i in range(N) : 
  for start in range(N) : 
    end = start + i
    if end >= N : 
      break

    if i == 0 : 
      dp[start][end] = True
      continue
    
    if i == 1 : 
      if num[start] == num[end] : 
        dp[start][end] = True
        continue
    
    if num[start] == num[end] and dp[start + 1][end - 1] : 
      dp[start][end] = True



M = int(input())
for i in range(M) : 
  S, E = map(int, input().split())
  if dp[S - 1][E - 1] : 
    print(1)
  else : 
    print(0)
