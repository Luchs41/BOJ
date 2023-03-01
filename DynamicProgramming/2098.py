# BOJ 2098
# 외판원 순회

import sys
input = sys.stdin.readline
n = int(input())
INF = 1e9

matrix = []
for _ in range(n) : 
  line = list(map(int, input().split()))
  matrix.append(line)



mem = [[-1] * (1 << n) for _ in range(n)]


def dfs(x, visited) : 
  if visited == (1 << n) - 1 : 
    if matrix[x][0] == 0 : 
        return INF
    mem[x][visited] = matrix[x][0]
    return matrix[x][0]

  if mem[x][visited] != -1 : 
    return mem[x][visited]

  temp = INF
  for i in range(n) : 
    if not visited & (1 << i) and matrix[x][i] != 0 : 
      temp = min(temp, matrix[x][i] + dfs(i, visited | (1 << i)))
  
  mem[x][visited] = temp
  return temp

print(dfs(0, 1))