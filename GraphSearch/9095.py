# BOJ 9095
# 입력받은 정수를 1, 2, 3의 합으로 나타내는 방법의 수를 출력
# 순서 상관 O (1+2, 2+1 -> 2가지)
# BFS 했어요

from collections import deque
def BFS(n) : 
  result = 0
  dx = [-1, -2, -3]
  q = deque()
  q.append(n)
  while q : 
    cur = q.popleft()
    if cur == 0 : 
      result += 1
    else : 
      for x in dx : 
        if cur + x >= 0 : 
          q.append(cur + x)
  return result


  

T = int(input())

for _ in range(T) : 
  n = int(input())
  print(BFS(n))