# BOJ 5014
# 총 F층, 목표 G층, 시작 S층
# 위로 U층, 아래로 D층 이동가능
# 엘리베이터로 못간다면 문자열 출력

from collections import deque

error = "use the stairs"

f, s, g, u, d = map(int, input().split())
visited = [0 for _ in range(0, f + 1)]
q = deque()
q.append(s)
res = -1
visited[s] = 1
while q:
  cur = q.popleft()

  if cur == g:
    res = visited[cur] - 1
    break
  else:
    for n in (cur + u, cur - d):
      if (0 < n <= f) and visited[n] == 0:
        visited[n] = visited[cur] + 1
        q.append(n) 

def bfs():  
    queue = deque()  
    queue.append(s)  

    check[s] = 1  

    while queue:  
        y = queue.popleft()  

        if y == g:  
            return check[y] - 1  
        else:  
            for x in (y + u, y - d):  
                if (0 < x <= f) and check[x] == 0:  
                    check[x] = check[y] + 1  
                    queue.append(x)  

    return "use the stairs"
if res != -1:
  print(res)
else:
  print(error)