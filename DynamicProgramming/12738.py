# BOJ 12738
# LIS

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