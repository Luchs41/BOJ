# BOJ 1149
# 1차원 거리에 1~N개의 집을 칠해야 함
# 빨초파 중 하나로 칠하며 각각 칠하는 비용이 다름
# 인접한 집이 같은 색이면 안될 때, 모든 집을 칠하는 최소의 비용 구하기

import sys
input = sys.stdin.readline
N = int(input())
r, g, b = 0, 0, 0
for _ in range(N) : 
  new = list(map(int, input().split()))
  newr = min(new[0] + g, new[0] + b)
  newg = min(new[1] + r, new[1] + b)
  newb = min(new[2] + r, new[2] + g)
  r = newr
  g = newg
  b = newb
  # print("r, g, b : ", r, g, b)
print(min(r, g, b))

