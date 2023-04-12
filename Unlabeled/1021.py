# BOJ 1021
# 회전하는 큐
# deque 이용해서 풀어봅시다. 

import sys
from collections import deque


def shift_left(dq : deque) : 
  dq.append(dq.popleft())

def shift_right(dq : deque) : 
  dq.appendleft(dq.pop())

N, M = map(int, input().split())
targets = deque(map(int, input().split()))
numbers = deque(range(1, N + 1))
shift_count = 0

for i in targets : 
  while True : 
    if numbers[0] == i : 
      numbers.popleft()
      break
    else : 
      if numbers.index(i) < len(numbers) / 2 : 
        while numbers[0] != i : 
          shift_left(numbers)
          shift_count += 1
      else : 
        while numbers[0] != i : 
          shift_right(numbers)
          shift_count += 1

print(shift_count)