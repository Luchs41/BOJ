# BOJ 12865
# 가능한 무게 내에서 최대의 가치 출력
# 0-1 knapsack problem : 이 물건을 담기 or 안 담기

import sys
input = sys.stdin.readline

# 물품의 수 N, 버틸 수 있는 무게 K
N, K = map(int, input().split())
item = [[0, 0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
  item.append(list(map(int, input().split())))

for i in range(1, N + 1):
  for j in range(1, K + 1):
    weight = item[i][0]
    value = item[i][1]
    # 현재 물건의 무게가 가용한 무게보다 크면, 이전 물건의 값 가져옴
    if j < weight:
      knapsack[i][j] = knapsack[i - 1][j]
    # 현재 물건을 담을 수 있으면, 현재 물건의 가치 + 이전 상태의 가치 합 VS 이전 물건의 값
    else:
      knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[-1][-1])