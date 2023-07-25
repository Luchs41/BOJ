# BOJ 3830
# 교수님은 기다리지 않는다
# 첫 줄에는 샘플의 개수와 한 일의 수가 주어진다. 
# ! a b w -> 무게를 측정, b가 a보다 w만큼 무겁다는 뜻
# ? a b -> b가 a보다 얼마나 무거운지 출력하라는 뜻
# 차이를 계산할 수 있다면 차이를 출력, 없다면 UNKNOWN을 출력
# 현재 노드의 값, 부모 노드, 부모 노드의 값을 저장
# union하는 경우, (a b의 차) - w만큼 a에 대해 업데이트, a의 부모를 b의 부모에 포함
# find하는 경우, 현재 부모 노드와 부모 노드의 값을 저장, 부모 노드가 바뀌었다면 업데이트

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def union(x, y, w) : 
  value[x] -= w
  parent[x] = y
  parentValue[x] = value[y]

def find(x) : 
  if parent[x] != x : 
    p, pv = parent[x], parentValue[x]
    parent[x] = find(p)
    value[x] += value[p] - pv
    parentValue[x] = value[parent[x]]
  return parent[x]

while 1 : 
  n, m = map(int, input().split())
  if n == 0 : 
    break
  parent = [i for i in range(n + 1)]
  value = [0] * (n + 1)
  parentValue = [0] * (n + 1)

  for _ in range(m) : 
    line = list(input().split())
    if line[0] == '!' : 
      a, b, w = int(line[1]), int(line[2]), int(line[3])
      if find(a) != find(b) : 
        union(parent[a], parent[b], w - value[b] + value[a])
    else : 
      a, b = int(line[1]), int(line[2])
      print(value[b] - value[a] if find(a) == find(b) else "UNKNOWN")
    

    