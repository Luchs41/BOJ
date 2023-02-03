# BOJ 1764
# 듣도 못한 사람의 명단과 보도 못한 사람의 명단이 주어질 때
# 듣도 보도 못한 사람의 명단을 구하는 프로그램
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
noListenSee = dict()
result = []
for i in range(N) : 
  name = input().rstrip()
  noListenSee[name] = True

for i in range(M) : 
  name = input().rstrip()
  if noListenSee.get(name, False) == True : 
    result.append(name)
result.sort()
print(len(result))
for name in result : 
  print(name)
