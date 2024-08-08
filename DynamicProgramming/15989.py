# BOJ 15989
# 1, 2, 3 더하기 4
# 주어진 숫자를 1, 2, 3의 합으로 나타낼 수 있는 경우의 수 세기
# 합을 이루는 수의 순서만 다른 경우는 같은 것으로 센다
# dp[i][k] : i를 더하기로 나타냈을 때, k로 끝나는 경우 (k = 1, 2, 3)
# 2차원 배열을 이용한 DP
T = int(input())
dp = [[0 for j in range(4)] for i in range(10001)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, 10001):
  dp[i][1] = dp[i - 1][1]
  dp[i][2] = dp[i - 2][1] + dp[i - 2][2]
  dp[i][3] = dp[i - 3][1] + dp[i - 3][2] + dp[i - 3][3]

for _ in range(T):
  n = int(input())
  print(sum(dp[n]))