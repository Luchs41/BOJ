# BOJ 1629
# A, B, C를 입력받아서 A의 B제곱을 C로 나눈 나머지를 출력한다. 

import sys

A, B, C = map(int, sys.stdin.readline().split())
def cal(A, B, C) : 
    if B == 1 : 
        return A % C
    else : 
        x = cal(A, B // 2, C)
        if B % 2 == 0:
            return x*x % C
        else : 
            return x * x * A % C

print(cal(A, B, C))