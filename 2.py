from collections import deque
def solution(edges):
  answer = []
  max_v = 0
  for i in edges:
    for j in i:
      max_v = max(max_v, j)
  

  graph = [[0] * (max_v+1) for _ in range(max_v + 1)]
  for edge in edges:
    source, dest = edge
    graph[source][dest] = 1
  
  # 생성된 노드 구하기
  added_node = 0
  for node in range(1, max_v + 1):
    out = 0 # 자신에게서 나가는 길
    to = 0 # 자신으로 꽂히는 길
    for i in range(1, max_v + 1):
      if graph[node][i] == 1: #자신에게서 나가는 길
        out += 1
      if graph[i][node] == 1: #자신에게 꽂히는 길
        to += 1
    if to == 0 and out >= 2:
      added_node = node

  def traverse(start):
    # start에서 출발해서 탐색
    # 탐색한 정점 번호를 set으로 반환
    visit = [0] * (max_v+1)
    q = deque()
    q.append(start)
    while q:
      cur = q.popleft()
      visit[cur] = 1
      for i in range(1, max_v+1):
        if graph[cur][i] == 1:
          if visit[i] == 0:
            q.append(i)
          else:
            visit[i] += 1
          
    
    # print(start,cur, visit)
    return visit
  
  candidates = []
  for i in range(1, max_v + 1):
    if graph[added_node][i] == 1:
      candidates.append(i)
  
  stick = 0
  doughnut = 0
  eight = 0
  for node in candidates:
    v = traverse(node)
    if all(num == 1 or num == 0 for num in v):
      stick += 1
      continue
    
    sum_e = sum(v)
    count = 0
    for num in v:
      if num != 0:
        count += 1
    # print(count, sum_e)
    if count == sum_e - 1:
      doughnut += 1
    if count == sum_e - 2:
      eight += 1
  answer = [added_node, doughnut, stick, eight]  
  return answer

edges = [[2, 3], [4, 3], [1, 5],[5,6],[6,1], [2, 1]]
edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8], [2, 13]]
print("-----\nSol : {}".format(solution(edges)))