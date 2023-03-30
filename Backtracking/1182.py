# BOJ 1182
# 부분수열의 합
# N개로 이루어진 수열 -> 크기가 양수인 부분수열 중 원소의 총합이 S가 되는 경우의 수를 구해라
# 브루트포스 + 백트래킹

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
a = list(map(int, input().split()))
result = 0
def subsetSum(index, Sum) : 
  global result
  if index >= N : 
    return

  Sum += a[index]
  if Sum == S : 
    result += 1
  
  subsetSum(index + 1, Sum)
  subsetSum(index + 1, Sum - a[index])

subsetSum(0, 0)
print(result)
