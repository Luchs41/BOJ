# BOJ 2473
# 세 용액
# 세 가지 용액을 혼합하여 가장 0에 가깝게 만들기
# N개의 정렬되지 않은 정수가 주어짐
# 하나 고정하고 투포인터로 해결
import sys
input = sys.stdin.readline
N = int(input())
liquid = sorted(list(map(int, input().split())))
result = int(1e10)
answer = []
for i in range(N-2) : 
  left = i + 1
  right = N - 1
  while left < right : 
    Sum = liquid[i] + liquid[left] + liquid[right]
    if abs(Sum) <= abs(result) : 
      answer = [liquid[i], liquid[left], liquid[right]]
      result = Sum
    if Sum < 0 : 
      left += 1
    elif Sum > 0 : 
      right -= 1
    else : 
      break
      
print(answer[0], answer[1], answer[2])