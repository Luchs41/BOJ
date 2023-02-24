# BOJ 15663
# N과 M -> N개의 자연수 중에서 M개를 고른 수열

import itertools
from collections import deque
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))


result = set(itertools.permutations(numbers, M))
result = sorted(deque(result))
for a in result : 
  for num in a : 
    print(num, end = " ")
  print()
