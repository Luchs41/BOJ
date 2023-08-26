# BOJ 13549
# 숨바꼭질 3
# 위치 N에서 K로 가는 최단시간 구하기
# 걷기 : 1초 뒤 X-1 또는 X+1로 이동
# 순간이동 : 0초 뒤 2*X로 이동
# DP인가? 싶었지만 BFS
# 순간이동을 우선적으로 고려해야 하므로, appendleft
# walk = [cur + 1, cur - 1]로 하니까 틀림 -> 뒤로 갔다 순간이동 하는게 우선이 되도록 순서 변경

from collections import deque
n, k = map(int, input().split())
road = [-1] * 100001
road[n] = 0

def bfs(n) : 
  q = deque()
  q.append(n)
  while q : 
    cur = q.popleft()
    
    if cur == k : 
      print(road[cur])
      break
    tp = cur * 2
    if 0 < tp < 100001 and road[tp] == -1 : 
      road[tp] = road[cur]
      q.appendleft(tp)
    walk = [cur - 1, cur + 1]
    for w in walk : 
      if 0 <= w < 100001 and road[w] == -1 : 
        road[w] = road[cur] + 1
        q.append(w)
    
    
bfs(n)
