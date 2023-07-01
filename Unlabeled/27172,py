# BOJ 27172
# 수 나누기 게임
# 1~1,000,000 사이의 수가 적힌 서로 다른 카드 -> 한장씩 나눠가짐
# 플레이어의 카드로 다른 플레이어의 수를 나눴을 때 나누어 떨어지면 승리
# 반대로 상대방 수로 내 카드의 수가 나누어 떨어지면 패배, 둘다 아니면 무승부
# 승리 +1점, 패배 -1점, 무승부는 변화x
# 본인 제외 모두와 결투를 하면 게임이 종료
# 플레이어 수와 각 플레이어 숫자가 주어졌을 때, 게임이 종료된 후의 모든 플레이어의 점수를 출력
# 각 쌍마다 모두 검사하면 느림 -> 자기 자신의 배수에 해당하는 값들을 검사하는 방식으로
import sys
input = sys.stdin.readline

N = int(input())
players = list(map(int, input().split()))
scores = [0] * 1000001
cards = [0] * 1000001
for i in range(0, N) : 
  cards[players[i]] = 1



for i in range(0, N) : 
  for j in range(players[i] * 2, 1000001, players[i]) : 
    if cards[j] == 1 : 
      scores[players[i]] += 1
      scores[j] -= 1

for i in range(N) : 
  print(scores[players[i]], end=" ")
print()