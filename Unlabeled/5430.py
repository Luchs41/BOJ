# BOJ 5430
# 문제 생략

import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t) : 
  p = list(input().rstrip())
  n = int(input())
  flagR = False
  error = False
  data = input().strip('[').strip()
  data = data[:len(data) - 1]
  data = list(data.split(','))
  if n > 0 : 
    data = deque(map(int, data))
  else : 
    data = deque(data)
    data.pop()
  for cmd in p : 
    if cmd == 'R' : 
      flagR = not flagR
    elif cmd == 'D' : 
      if not data : 
        print("error")
        error = True
        break
      else : 
        if flagR == False : 
          data.popleft()
        else : 
          data.pop()
  if error == False : 
    print('[', end="")
    while data : 
      if flagR == False : 
        print(data.popleft(), end="")
      else : 
        print(data.pop(), end="")
      if data : 
        print(',', end="")
    print(']')
    
