# BOJ 10845
# 큐 구현
from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
q = deque()
for i in range(N) : 
  cmd = input().rstrip().split()
  if len(cmd) == 2 : 
    q.append(int(cmd[1]))
  else : 
    if cmd[0] == 'pop' : 
      print(q.popleft()) if len(q) != 0 else print(-1)
    elif cmd[0] == 'size' : 
      print(len(q))
    elif cmd[0] == 'empty' : 
      print(1) if len(q) == 0 else print(0)
    elif cmd[0] == 'front' : 
      print(q[0]) if len(q) != 0 else print(-1)
    elif cmd[0] == 'back' : 
      print(q[len(q)-1]) if len(q) != 0 else print(-1)