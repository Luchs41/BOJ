# BOJ 1725
# BOJ 6549랑 같은문제,,

# BOJ 6549
# 히스토그램에서 가장 큰 직사각형
# 직사각형의 수, 각 직사각형의 높이가 주어진다. 
# 가장 큰 직사각형의 넓이를 출력한다. 
# 1 <= 갯수 <= 100,000 / 0 <= 높이 <= 10^9



import sys
from collections import deque
input = sys.stdin.readline

while 1 : 
  n = int(input())
  rec = []
  for _ in range(n) : 
    rec.append(int(input()))
  Max = 0
  stack = deque()

  for i in range(n) : 
    while len(stack) != 0 and rec[stack[-1]] > rec[i] : 
      temp = stack.pop()
      if len(stack) == 0 : 
        length = i
      else : 
        length = i - stack[-1] - 1
      Max = max(Max, length * rec[temp])
    stack.append(i)
  while len(stack) != 0 : 
    temp = stack.pop()

    if len(stack) == 0 : 
      length = n
    else : 
      length = n - stack[-1] - 1
    Max = max(Max, length * rec[temp])

  print(Max)
  break

  