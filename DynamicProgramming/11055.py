# BOJ 11055
# 가장 큰 증가하는 부분 수열의 합

n = int(input())
arr = list(map(int, input().split()))
d = [1 for _ in range(n)]
d[0] = arr[0]

for i in range(1, n):
  for j in range(i):
    if arr[i] > arr[j]:
      d[i] = max(d[i], d[j] + arr[i])
    else:
      d[i] = max(d[i], arr[i])
print(max(d))