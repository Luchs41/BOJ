# BOJ 10773
# 첫 줄에 정수 K가 주어진다. 
# 이후 K개의 줄에 정수가 차례대로 주어진다. 0이 아닌 수라면 그 수를 장부에 적고, 0이라면 가장 최근에 적은 숫자를 지운다. 
# 최종적으로 장부에 남은 수의 합을 출력한다. 

import sys
from collections import deque
jangbu = deque()
K = int(input())
for _ in range(K) : 
    num = int(sys.stdin.readline().strip())
    if num == 0 : 
        jangbu.pop()
    else : 
        jangbu.append(num)

print(sum(jangbu))