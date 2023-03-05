# BOJ 14889
# 스타트와 링크
# 축구하려고 N명이 모임 -> N은 짝수
# S_ij -> i번 사람과 j번 사람이 같은 팀에 속했을 때 팀에 더해지는 능력치
# 팀의 능력치 차이의 최솟값 출력
# N을 두 개로 잘 분할해야
N = int(input())
member = []
for _ in range(N) : 
  member.append(list(map(int, input().split())))

visited = [0] * N
Min = 1e9
def DFS(depth, start) : 
  global Min
  if depth == N / 2 : 
    powerS = 0
    powerL = 0
    for i in range(N) : 
      for j in range(N) : 
        if visited[i] == 1 and visited[j] == 1 : 
          powerS = powerS + member[i][j]
        elif visited[i] == 0 and visited[j] == 0 : 
          powerL = powerL + member[i][j]
    Min = min(Min, abs(powerL - powerS))
    
    return

  for i in range(start, N) : 
    if visited[i] == 1 : 
      continue
    visited[i] = 1
    DFS(depth + 1, i + 1)
    visited[i] = 0

DFS(0, 0)
print(Min)