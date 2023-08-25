# BOJ 9655
# 돌 게임
# 돌 N개 -> 1개 또는 3개 가져갈 수 있음
# 마지막 돌을 가져가면 이김
# 상근 선턴 -> 상근이가 이기면 SK, 창영이가 이기면 CY
# 엥 그냥 홀짝
n = int(input())
if n % 2 == 0 : 
  print('CY')
else : 
  print("SK")