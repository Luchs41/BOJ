# BOJ 14888
# 연산자 끼워넣기
# 주어진 수열의 순서를 유지한 채, 수 사이에 연산자를 넣는다. 
# 만들 수 있는 최대값과 최소값을 찾는다. 
# 모든 경우의 수를 봐야하겠다. -> DFS

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

Max = -1e9
Min = 1e9

def DFS(total, depth, plus, minus, mul, div) : 
  global Max, Min
  if depth == n : 
    Max = max(Max, total)
    Min = min(Min, total)
    return
  
  if plus > 0 : 
    DFS(total + A[depth], depth + 1, plus - 1, minus, mul, div)
  if minus > 0 : 
    DFS(total - A[depth], depth + 1, plus, minus - 1, mul, div)
  if mul > 0 : 
    DFS(total * A[depth], depth + 1, plus, minus, mul - 1, div)
  if div > 0 : 
    DFS(int(total / A[depth]), depth + 1, plus, minus, mul, div - 1)
  

DFS(A[0], 1, op[0], op[1], op[2], op[3])

print(Max)
print(Min)