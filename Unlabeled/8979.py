# BOJ 8979
# 올림픽 메달 순위
# 1. 금메달 수
# 2. 금메달 수가 같으면, 은메달 수
# 3. 금, 은메달 수가 같으면, 동메달 수
# 4. 셋 다 같으면, 같은 등수 -> 다음 등수는 블랭크
# 자료구조에 팀번호, 금, 은, 동 때려넣고 정렬
# 현재 등수 설정하고 쭉 선회하면서 진행

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
info = list()
for _ in range(N):
  info.append(list(map(int, input().split())))
info = sorted(info, key = lambda x: (-x[1], -x[2], -x[3]))

idx = [info[i][0] for i in range(N)].index(K)

for i in range(N):
  if info[idx][1:] == info[i][1:]:
    print(i + 1)
    break

