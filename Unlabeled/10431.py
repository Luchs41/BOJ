# BOJ 10431
# 줄세우기
# 1 2 3 5 6 << 4 : 5
# 1 2 3 4 5 6 : 3
# 정렬 전의 인덱스와 정렬 후의 인덱스의 차이를 누적?
# 각 줄 맨 앞 번호를 안빼버린
import sys
input = sys.stdin.readline

P = int(input())
result = ""
for i in range(P):
  steps = 0
  arr = list(map(int, input().split()))
  arr = arr[1:]
  sortedArr = list()
  for num in arr:
    sortedArr.append(num)
    idxBefore = len(sortedArr) - 1
    sortedArr = sorted(sortedArr)
    idxAfter = sortedArr.index(num)
    steps += idxBefore - idxAfter
  result += "{} {}\n".format(i + 1, steps)

print(result)