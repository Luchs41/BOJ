# BOJ 25757
# 미니게임
# 전체 플레이어 리스트 -> 중복 제거
# 게임당 플레이 가능한 사람 숫자 - 1로 나눈 몫이 답

import sys
input = sys.stdin.readline
games = ['Y', 'F', 'O']
players, gameType = input().split()
players = int(players)

maxPlayers = games.index(gameType) + 2

playerList = list()
for _ in range(players):
  playerList.append(input().strip())
playerList = set(playerList)

answer = len(playerList) // (maxPlayers - 1)
print(answer)