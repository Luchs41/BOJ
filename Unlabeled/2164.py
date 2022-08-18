# BOJ 2164
# 1~N까지 순서대로 쌓인 카드더미에서, 맨 위의 장을 버리고 새로 맨 위의 장이 된 카드를 가장 아래로 두는 행위를 반복
# 마지막에 남는 카드는?
from collections import deque

N = int(input())
q = deque(range(1, N + 1))

while len(q) > 1 : 
    q.popleft()
    move = q.popleft()
    q.append(move)
print(q[0])