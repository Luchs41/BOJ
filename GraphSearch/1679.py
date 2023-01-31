# BOJ 1679
# 수빈이의 위치 N과 동생의 위치 K가 주어진다. 
# 수빈이는 매 초 이동 Or 순간이동
# 이동 -> 좌표 + 1 Or 좌표 - 1
# 순간이동 -> 좌표 * 2
# 동생을 찾을 수 있는 가장 빠른 시간 출력
from collections import deque

def BFS(N, K) : 
  
  q = deque()
  q.append(N)
  while q : 
    cur = q.popleft()
    if cur == K : 
      return depth[cur]
    for i in (cur - 1, cur + 1, cur * 2) : 
      if 0 <= i <= limit and depth[i] == 0 : 
        depth[i] = depth[cur] + 1
        q.append(i)

      
N, K = map(int, input().split())
limit = 100000
depth = [0] * (limit + 1)
print(BFS(N, K))
