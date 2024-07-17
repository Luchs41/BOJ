import itertools
def solution(dice):
  n = len(dice)
  dice_combination = itertools.combinations(list(range(0, n)), n//2)
  
  all_dice = set(range(0, n))
  A_comb = []
  B_comb = []
  for c in dice_combination:
    A_comb.append(c)
    B_comb.append(tuple(all_dice.difference(set(c))))
  
  total_case = len(A_comb)
  wins = [0] * total_case
  all_combinations = list(itertools.product(*dice))
  
  for i in range(total_case):
    a = A_comb[i]
    b = B_comb[i]
    for case in all_combinations:
      a_sum = 0
      b_sum = 0
      for an in a:
        a_sum += case[an]
      for bn in b:
        b_sum += case[bn]
      if a_sum > b_sum:
        wins[i] += 1
  
  winCom = 0
  
  for idx in range(total_case):
    if wins[idx] > wins[winCom]:
      winCom = idx
  answer = []
  for d in A_comb[winCom]:
    answer.append(d+1)
  
  return answer


dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
solution(dice)