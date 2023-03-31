# BOJ 1208
# 부분수열의 합 2
# N개로 이루어진 수열 -> 크기가 양수인 부분수열 중 원소의 총합이 S가 되는 경우의 수를 구해라
# 1182.py에 비해 N이 증가했다. -> 시간초과가 날 것이다.
# 주어진 수열을 반으로 나누어서 각각의 부분수열의 합을 구한다.

import sys
from itertools import combinations
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


N, S = map(int, input().split())
arr = list(map(int, input().split()))

left = arr[:N//2]
right = arr[N//2:]

left_sum = []
right_sum = []

for i in range(len(left)+1):
    left_sum.extend(list(combinations(left, i)))
for i in range(len(right)+1):
    right_sum.extend(list(combinations(right, i)))

left_sum = [sum(i) for i in left_sum]
right_sum = [sum(i) for i in right_sum]

left_sum.sort()
right_sum.sort()

answer = 0
for i in left_sum:
    answer += bisect_right(right_sum, S-i) - bisect_left(right_sum, S-i)

if S == 0:
    answer -= 1

print(answer)