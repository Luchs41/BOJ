# BOJ 11725
# 트리의 부모 찾기
# 트리의 루트를 1이라고 정했을 때, 2~N번 노드의 부모를 출력
# 트리를 DFS하며 이전 노드의 값을 parent로 설정
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1) : 
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

visited = [False for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]
def DFS(before) : 
  for vertex in tree[before] : 
    if visited[vertex] == False and parent[vertex] == 0 : 
      parent[vertex] = before
      visited[vertex] = True
      DFS(vertex)
      visited[vertex] = False
visited[1] = True
DFS(1)

for i in range(2, N + 1) : 
  print(parent[i])