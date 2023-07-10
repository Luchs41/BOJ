# BOJ 14725
# 개미굴
# 트리 아래로 내려가면서 만나는 정보들을 입력으로 받는다
# 로봇 개미의 수는 충분한 만큼
# 그 정보를 토대로 트리의 구조를 출력, depth는 '--'으로 구분

import sys
input = sys.stdin.readline

n = int(input())
ant = []
for i in range(n) : 
  line = list(input().split())
  ant.append(line[1:])

ant.sort()
depth = '--'
result = []

for i in range(n) : 
  # root가 처음 나올 때는 다 출력하면 된다. 
  if i == 0 : 
    for j in range(len(ant[i])) : 
      result.append(depth * j + ant[i][j])
  # root를 공유하는경우, 처음 나오는 분기부터 출력하면 된다. 
  else : 
    idx = 0
    for j in range(len(ant[i])) : 
      if ant[i - 1][j] != ant[i][j] or len(ant[i - 1]) <= j : 
        break
      else : 
        idx = j + 1
    for j in range(idx, len(ant[i])) :  
      result.append(depth * j + ant[i][j])


for a in result : 
  print(a)