# BOJ 20125
# 쿠키의 신체 측정
# 각 부위의 너비는 1
# 머리는 심장 바로 위 1칸
# 심장 위치 찾고 사지 길이 찾기

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
# 심장찾기
heart = -1
for i in range(N):
  for j in range(N):
    if graph[i][j] == '*':
      heart = (i+1, j)
      break
  if not heart == -1:
    break

# 1씩 더해서 출력
print(heart[0] + 1, heart[1] + 1)
# 왼팔 오른팔 허리 왼다리 오른다리
ny = heart[1]
left = 0
while 1:
  if 0 <= ny - 1 < N and graph[heart[0]][ny - 1] == '*':
    left += 1
    ny -= 1
  else:
    break

# 오른팔
ny = heart[1]
right = 0
while 1:
  if 0 <= ny + 1 < N and graph[heart[0]][ny + 1] == '*':
    right += 1
    ny += 1
  else:
    break
# 허리
nx = heart[0]
waist = 0
while 1:
  if 0 <= nx + 1 < N and graph[nx + 1][heart[1]] == '*':
    waist += 1
    nx += 1
  else:
    break
# 왼다리
nx = heart[0] + waist
leftleg = 0
while 1:
  if 0 <= nx + 1 < N and graph[nx + 1][heart[1] - 1] == '*':
    leftleg += 1
    nx += 1
  else:
    break

# 오른다리
nx = heart[0] + waist
rightleg = 0
while 1:
  if 0 <= nx + 1 < N and graph[nx + 1][heart[1] + 1] == '*':
    rightleg += 1
    nx += 1
  else:
    break
print(left, right, waist, leftleg, rightleg)