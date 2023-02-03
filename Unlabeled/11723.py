# BOJ 11723
# 집합 구현
import sys
input = sys.stdin.readline
M = int(input())
s = 0b0

for _ in range(M) : 
  cmd = input().rstrip().split()
  if len(cmd) == 2 : 
    cmd[1] = int(cmd[1])
    if cmd[0] == 'add' : 
      s = s | (0b1 << cmd[1])
    elif cmd[0] == 'remove' : 
      s = s & ~(0b1 << cmd[1])
    elif cmd[0] == 'check' : 
      print(1) if (s & 0b1 << cmd[1]) else print(0)
    elif cmd[0] == 'toggle' : 
      s = s ^ (0b1 << cmd[1])
    
  else : 
    if cmd[0] == 'all' : 
      s = 0b111111111111111111111
    elif cmd[0] == 'empty' : 
      s = 0b0
  