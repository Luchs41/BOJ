# BOJ 9935
# 문자열 폭발
# 문자열에 폭발 문자열이 포함된 경우, 해당 부분이 사라진다. 
# 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다. 
# 모든 폭발이 끝난 후 어떤 문자열이 남는지 구한다. 남아있는 문자가 없으면 FRULA를 출력

import sys
input = sys.stdin.readline
from collections import deque

s = input().strip()
b = input().strip()

stack = []
length = len(b)
last = b[-1]

for char in s : 
  stack.append(char)
  if char == last and ''.join(stack[-len(b) : ]) == b : 
    del stack[-len(b) : ]

if stack : 
  print(''.join(stack))
else : 
  print("FRULA")
  