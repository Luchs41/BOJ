# BOJ 15664
# N과 M(10)
# N개의 자연수 중 M개를 고른 수열 중 비내림차순인 수열을 모두 출력
# 수열은 사전순으로 출력
# DFS로 순회하며 찾기 -> 백트래킹

import sys

input = sys.stdin.readline

def dfs(start) : 
  if len(temp) == m : 
    print(*temp)
    return
  last = 0
  for i in range(start, n) : 
    if visited[i] == 0 and last != nums[i] : 
      visited[i] = 1
      temp.append(nums[i])
      last = nums[i]
      dfs(i+1)
      visited[i] = 0
      temp.pop()




n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0] * n
temp = list()

dfs(0)