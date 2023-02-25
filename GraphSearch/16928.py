# BOJ 16928
# 뱀과 사다리 게임
# 첫 줄에 사다리와 뱀의 갯수가 주어지고, 나머지는 사다리와 뱀의 정보
# 1번칸에서 시작하여 100번으로 가는 경우의 수를 탐색

import sys
input = sys.stdin.readline
from collections import deque
dice = [1, 2, 3, 4, 5, 6]

N, M = map(int, input().split())
ladder = dict()
snake = dict()
for _ in range(N) : 
  start, end = map(int, input().split())
  ladder[start] = end
for _ in range(M) : 
  start, end = map(int, input().split())
  snake[start] = end

def BFS() : 
  visit = [False] * 101
  q = deque()
  q.append((1, 0))
  visit[1] = True
  while q : 
    cur, depth = q.popleft()
    if cur == 100 : 
      print(depth)
      return
    for i in dice : 
      new = cur + i
      if new <= 100 and visit[new] == False : 
        if new in ladder.keys() : 
          new = ladder[new]
        if new in snake.keys() : 
          new = snake[new]
        
        if visit[new] == False : 
          q.append((new, depth + 1))
          visit[new] = True

BFS()