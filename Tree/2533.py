# BOJ 2533
# SNS
# 주어진 그래프에서 모든 개인이 새로운 아이디어를 수용하기 위해 필요한 최소 얼리 아답터의 수를 구하시오
# 얼리 아답터가 아닌 사람들은 자신의 모든 친구가 얼리 아답터일 때 새로운 아이디어를 받아들인다. 
# Tree + DP
# DFS를 통해 리프 노드까지 간 다음, 리프에서 subtask를 해결하면서 root까지 올라온다. 

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())
c = [[] for i in range(N + 1)]
dp = [[0, 0] for i in range(N + 1)]

for _ in range(N - 1) : 
  a, b = map(int, input().split())
  c[a].append(b)
  c[b].append(a)

visited = [False for i in range(N + 1)]

def dfs(start) : 
  visited[start] = True
  if len(c[start]) == 0 : 
    dp[start][1] = 1
    dp[start][0] = 0
  else : 
    for i in c[start] : 
      if visited[i] == False : 
        dfs(i)
        dp[start][1] += min(dp[i][0], dp[i][1])
        dp[start][0] += dp[i][1]
    dp[start][1] += 1

dfs(1)
print(min(dp[1][0], dp[1][1]))
