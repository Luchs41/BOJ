# BOJ 15654
# N과 M -> N개의 자연수 중에서 M개를 고른 수열
import itertools
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

result = list(itertools.permutations(numbers, M))
result.sort()

for i in result : 
  for j in i : 
    print(j, end=" ")
  print()