# BOJ 11279
# 최대 힙 문제
# 연산의 개수 N과 이후 x가 N줄에 주어진다. 
# x가 자연수 -> 힙에 추가
# x가 0 -> 힙의 최대값을 출력하고 그 값을 제거

import sys
import heapq
input = sys.stdin.readline
N = int(input())
s = []

for i in range(N) : 
  x = int(input())
  if x == 0 : 
    print(0) if len(s) == 0 else print(-heapq.heappop(s))
  else : 
    heapq.heappush(s, -x)
  
