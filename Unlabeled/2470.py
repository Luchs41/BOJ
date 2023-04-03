# BOJ 2470
# 용액의 양이 주어졌을 때, 두 용액의 합이 0에 가장 가까운 용액을 찾는다.
# BOJ 2467과 다르게, 용액이 정렬되어 있지 않다.

import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort() # 용액을 정렬한다.
left = 0
right = len(liquid) - 1
result = abs(liquid[left] + liquid[right])
result_left = left
result_right = right

while left < right : 
  Sum = liquid[left] + liquid[right]
  if abs(Sum) < result : 
    result = abs(Sum)
    result_left = left
    result_right = right

    if Sum == 0 : break
  
  if Sum < 0 : 
    left += 1
  else : 
    right -= 1

print(liquid[result_left], liquid[result_right])