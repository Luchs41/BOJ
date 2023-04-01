# BOJ 1806
# 부분합
# 10000개의 자연수로 이루어진 수열이 주어진다.
# 이 수열에서 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중, 그 합이 S 이상이 되는 것 중, 가장 짧은 것을 구해라.
# 합이 S 이상이 되는 것이 없다면 0을 출력한다.
# 투 포인터로 해결
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
i = 0
j = 0
cur_sum = arr[0]
cur_len = 1e7
while True : 
  if cur_sum >= S : 
    cur_len = min(cur_len, j - i + 1)
    cur_sum -= arr[i]
    i += 1
  else : 
    j += 1
    if j == N : 
      break
    cur_sum += arr[j]

if cur_len == 1e7 : 
  print(0)
else : 
  print(cur_len)