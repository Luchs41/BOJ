# BOJ 1978
# 주어진 N개의 수 중 소수가 몇 개인지 찾아서 출력
# 수는 1000 이하의 자연수
import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))

for num in A : 
    if num == 1 : 
        N -= 1
        continue
    for i in range(2, round(num**(1/2))+1) : 
        if num % i == 0 : 
            N -= 1
            break
print(N)