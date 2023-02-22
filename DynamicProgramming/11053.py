# BOJ 11053
# 가장 긴 증가하는 부분 수열
# 제일 큰 값 -> 끝에 추가
# 아니면 -> 이분탐색으로 들어갈 위치 찾기
# result가 LIS는 아님..길이만 찾기 가능
from collections import deque
n = int(input())
a = deque(map(int, input().split()))

result = list()
def binarySearch(left, right, target) : 
  while left < right : 
    mid = (left + right) // 2
    if (result[mid] < target) : 
      left = mid + 1
    else : 
      right = mid
  return right

result.append(a.popleft())
while a : 
  s = a.popleft()
  if s > result[len(result) - 1] : 
    result.append(s)
  else : 
    idx = binarySearch(0, len(result) - 1, s)
    result[idx] = s
  #print(result)

#print(result)
print(len(result))