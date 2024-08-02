# BOJ 9017
# 크로스 컨트리
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  count = {}
  temp = list(map(int, input().split()))
  
  for i in range(n):
    if temp[i] in count:
      count[temp[i]] += 1
    else:
      count[temp[i]] = 1

  # 6명 이하 팀 구하기
  dele = {}
  for k, v in count.items():
    if v < 6:
      dele[k] = 1

  team = {}
  idx = 1 # 점수
  for i in range(n):
    if temp[i] not in dele:
      if temp[i] in team:
        if team[temp[i]][0] < 4:
          team[temp[i]][0] += 1
          team[temp[i]][1] += idx
        elif team[temp[i]][0] == 4:
          team[temp[i]][0] += 1
          team[temp[i]][2] = idx
      else:
        team[temp[i]] = [1, idx, 0] # 사람 수, 상위 4명 합, 5번째 주자 점수
      idx += 1
  
  team = sorted(team.items(), key=lambda x:(x[1][1], x[1][2]))
  print(team[0][0])
  