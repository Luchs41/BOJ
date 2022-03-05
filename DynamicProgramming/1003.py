# BOJ 1003
# 피보나치를 수행하여 0이 출력되는 횟수(Fibo(0))와 1이 출력되는 횟수(Fibo(1))를 출력하는 문제. 
# N = 40까지의 피보나치를 미리 계산하여 입력되는 값에 해당하는 내용을 출력하는 식으로 구현.
from collections import deque
caseN = int(input())
fibo = deque()
fibo.append([1, 0])
fibo.append([0, 1])

for i in range(2, 41) : 
    fibo.append([fibo[i-2][0] + fibo[i-1][0], fibo[i-2][1] + fibo[i-1][1]])
for _ in range(caseN) : 
    N = int(input())
    print(fibo[N][0], fibo[N][1])