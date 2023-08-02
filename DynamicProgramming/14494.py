# BOJ 14494
# (1, 1)에서 (n, m)까지 도착하는 경우의 수 구하기
# 방향은 세가지 (→, ↓, ↘)
# DP


n, m = map(int, input().split())
div = int(1e9 + 7)
dir = [(1, 0), (0, 1), (1, 1)]
dp = [[0] * m for i in range(n)]

dp[0][0] = 1

for i in range(n) : 
  dp[i][0] = 1
for i in range(m) : 
  dp[0][i] = 1


for i in range(n) : 
  for j in range(m) : 
    if dp[i][j] == 0 : 
      for k in dir : 
        if i - k[0] >= 0 and j - k[1] >= 0 : 
          dp[i][j] += dp[i - k[0]][j - k[1]]

    
print(dp[n - 1][m - 1] % div)    