# BOJ 13458
# 시험 감독

import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0
for room in a : 
  room -= b
  result += 1
  if room < 0 : 
    continue
  else : 
    result += room // c
    if room % c != 0 : 
      result += 1

print(result)