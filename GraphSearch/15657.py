# BOJ 15657
# N과 M -> N개의 자연수 중에서 M개를 고른 수열인데 비내림차순

from collections import deque

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
result = deque()
def DFS(depth, start) : 
  if depth == M : 
    print(' '.join(map(str, result)))
    return
  for i in range(start, N) : 
    result.append(numbers[i])
    DFS(depth + 1, i)
    result.pop()

DFS(0, 0)