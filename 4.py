from collections import deque
def solution(coin, cards):

  def check(newHand):
    res = 0
    for c in newHand:
      if target - c in newHand:
        res += 1
    return res

  answer = 0
  n = len(cards)
  target = n + 1
  cards = deque(cards)
  # 미래시를 활용해서
  # n+1을 만들수있는 짝꿍이 언제 나오는지를 보고
  # 버틸수있으면 버텨보는 그런 시나리오
  # future[i] : i가 적힌 카드가 언제 나오는지
  # -1 -> 이미 사용 혹은 버림
  # 0 -> 멀리건 (0번째 ~ n/3 -1번째)
  # n -> n 라운드에 새롭게 뽑을 친구들
  hand = []
  future = [0] * (n + 1)
  r = 1
  for i in range(n // 3, n, 2):
    future[cards[i]] = r
    future[cards[i + 1]] = r
    r += 1
  r = 1
  for i in range(0, n // 3):
    hand.append(cards.popleft())
  
  
  

    
  
  return answer

coin = 4
cards = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]


print("------\nSolution = {}".format(solution(coin, cards)))