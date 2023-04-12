# BOJ 9466
# 텀 프로젝트
# 어느 팀에도 속하지 않는 학생들의 수를 계산
# 서로가 서로를 선택해야 팀 구성 가능
# 자기도 자신을 골라야 함
# DFS로 돌다가 -> 자기 자신 만나면 stop

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def dfs(x) : 
  global result
  visited[x] = True
  team.append(x)
  num = student[x]

  if visited[num] : 
    if num in team : 
      result += team[team.index(num) : ]
    return
  else : 
    dfs(num)


T = int(input())
for _ in range(T) : 
  n = int(input())
  student = [0]
  student += list(map(int, input().split()))
  visited = [True]
  visited += [False] * n
  result = list()

  for i in range(1, n + 1) : 
    if not visited[i] : 
      team = []
      dfs(i)
  print(n - len(result))

  
    
  
  
  