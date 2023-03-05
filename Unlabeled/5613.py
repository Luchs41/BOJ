# BOJ 5613
# 계산기 프로그램


import sys
input = sys.stdin.readline
from collections import deque

q = deque()

while 1 : 
  cmd = input().strip()
  if cmd == '=' : 
    break
  q.append(cmd)

total = 0
total += int(q.popleft())

while q : 
  cmd = q.popleft()
  if cmd == '+' : 
    total += int(q.popleft())
  elif cmd == '-' : 
    total -= int(q.popleft())
  elif cmd == '*' : 
    total = total * int(q.popleft())
  elif cmd == '/' : 
    total = int(total // int(q.popleft()))

print(total)