# BOJ 11726
# 2xn 크기의 직사각형을 1x2, 2x1 크기의 타일로 채우는 방법의 수를 구하는 프로그램
# 구한 수를 10007로 나눈 나머지를 출력

from collections import deque
n = int(input())

cases = [0] * 1001
cases[1] = 1
cases[2] = 2
for i in range(3, 1001) : 
  cases[i] = cases[i-1] + cases[i-2]
print(cases[n] % 10007)


