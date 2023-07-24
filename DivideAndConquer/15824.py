# BOJ 15824
# 캡사이신
# [5, 2, 8]의 스코빌 지수를 가진 음식을 먹을 때 -> 매운 정도는 최대값인 8에서 최소값인 2를 뺀 6만큼의 매운맛을 느낀다. 
# 이 음식점의 모든 조합을 먹어볼 때 매운 정도의 합을 구하라
# 분할 정복을 이용한 거듭제곱

import sys
input = sys.stdin.readline

def pow(a, b) : 
  if b == 0 : 
    return 1
  if b == 1 : 
    return a
  
  temp = pow(a, b // 2)
  return temp * temp % 1000000007 if b % 2 == 0 else temp * temp * a % 1000000007


n = int(input())
arr = sorted(list(map(int, input().split())))
answer = 0

for i in range(n) : 
  answer += arr[i] * (pow(2, i) - pow(2, n - i - 1))

print(answer % 1000000007)