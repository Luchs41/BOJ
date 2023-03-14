# BOJ 2467
# 용액
# 전체 용액 중 두 용액을 혼합하여 가장 0에 가까운 값을 출력한다. 
# 투포인터로 해결
import sys
input = sys.stdin.readline
N = int(input())
liquid = list(map(int, input().split()))
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