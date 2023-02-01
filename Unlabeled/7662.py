# BOJ 7662
# 이중 우선순위 큐를 구현
# 우선순위가 가장 높은 데이터 또는 낮은 데이터 중 하나를 삭제한다. 
# 입력데이터의 수 T가 첫줄에 주어짐
# 각 데이터의 첫 줄에는 Q에 적용할 연산의 개수
# 각 연산은 연산 문자(D나 I)와 정수 n이 주어짐
# I n -> 정수 n을 Q에 삽임
# D 1 -> Q에서 최댓값을 삭제 / D -1 -> Q에서 최솟값을 삭제
# 최댓값(최솟값)이 둘 이상 -> 하나만 삭제
# 최대 / 최소 힙을 각각 하나씩 -> 두개 사용해서
# 값의 삽입은 동시에 해주고
# 삭제할 때 동기화해주는 식으로
# 최종 출력 전에도 한번 동기화
import heapq
from sys import stdin

T = int(stdin.readline())
for _ in range(T) : 
  k = int(stdin.readline())
  minQ = []
  maxQ = []
  visited = [False] * 1000001
  for i in range(k) : 
    op = stdin.readline().split()
    if op[0] == 'I' : 
      heapq.heappush(minQ, (int(op[1]), i))
      heapq.heappush(maxQ, (-int(op[1]), i))
      visited[i] = True
    elif op[0] == 'D' : 
      if op[1] == '1' : 
        while maxQ and not visited[maxQ[0][1]] : 
          heapq.heappop(maxQ)
        if maxQ : 
          visited[maxQ[0][1]] = False
          heapq.heappop(maxQ)
      else : 
        while minQ and not visited[minQ[0][1]] : 
          heapq.heappop(minQ)
        if minQ : 
          visited[minQ[0][1]] = False
          heapq.heappop(minQ)
  while minQ and not visited[minQ[0][1]] : 
    heapq.heappop(minQ)
  while maxQ and not visited[maxQ[0][1]] : 
    heapq.heappop(maxQ)
  if minQ : 
    max = -maxQ[0][0]
    min = minQ[0][0]
    print(max, min)
  else : 
    print("EMPTY")