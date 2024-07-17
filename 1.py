def solution(friends, gifts):
  answer = 0
  
  name = dict()
  idx = 0
  for n in friends:
    name[n] = idx
    idx += 1
  
  n_friends = len(friends)
  board = [[0] * n_friends for _ in range(n_friends)]
  
  for g in gifts:
    A, B = g.split()
    A = name[A]
    B = name[B]
    board[A][B] += 1
  
  giftsPoint = [0] * n_friends # 선물 지수
  res = [0] * n_friends # 받게 될 선물 수

  # 선물 지수 계산
  for i in range(n_friends):
    for j in range(n_friends):
      giftsPoint[i] += board[i][j]
      giftsPoint[j] -= board[i][j]
  
  # 받을 선물 계산
  for i in range(n_friends):
    for j in range(i+1, n_friends):
      # 두 사람간의 기록이 있다면
      if board[i][j] != 0 or board[j][i] != 0:
        # 우열을 가릴 수 있다면
        if board[i][j] > board[j][i]:
          res[i] += 1
        elif board[i][j] < board[j][i]:
          res[j] += 1
        # 우열을 가릴 수 없다면
        else:
          # 선물지수로 판별 가능?
          if giftsPoint[i] > giftsPoint[j]:
            res[i] += 1
          elif giftsPoint[i] < giftsPoint[j]:
            res[j] += 1
          # 선물지수로 판별 안되면 그냥 X
      # 두 사람 간의 기록이 없다면
      else: 
        if giftsPoint[i] > giftsPoint[j]:
          res[i] += 1
        elif giftsPoint[i] < giftsPoint[j]:
          res[j] += 1
  
  
  answer = max(res)
  return answer
#friends = ["muzi", "ryan", "frodo", "neo"]
#gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

solution(friends, gifts)