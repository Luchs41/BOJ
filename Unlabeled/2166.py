# BOJ 2166
# 다각형의 면적
# N개의 점으로 이루어진 다각형의 면적을 구하시오. 
# 3 <= N <= 100,000, x, y좌표는 절댓값이 100,000을 넘지 않음
# 신발끈공식

import sys
input = sys.stdin.readline
N = int(input())
polygon = []
for _ in range(N) : 
  polygon.append(list(map(int, input().split())))
polygon.append(polygon[0])

result = 0
for i in range(N) : 
  result += (polygon[i][0] * polygon[i + 1][1]) - (polygon[i][1] * polygon[i + 1][0])

print(round(abs(result / 2), 1))