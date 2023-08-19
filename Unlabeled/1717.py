# BOJ 1717
# 첫째줄 : n, m -> 0~n 까지 n+1개의 집합, m개의 연산
# m개의 줄 : 0 a b -> a가 포함된 집합과 b가 포함된 집합을 합침
# 1 a b -> a와 b가 같은 집합에 포함되어 있는지를 확인
# disjoint set -> union-find


import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

def union(x, y) : 
  x = find(x)
  y = find(y)

  if x < y : 
    parent[y] = x
  else : 
    parent[x] = y

def find(x) : 
  if x == parent[x] : 
    return x
  parent[x] = find(parent[x])
  return parent[x]
  


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m) : 
  cmd, a, b = map(int, input().split())
  if cmd == 0 : 
    union(a, b)
  else : 
    if find(a) == find(b) : 
      print("YES")
    else :
      print("NO")