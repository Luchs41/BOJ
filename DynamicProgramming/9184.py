# BOJ 9184
# 주어진 재귀 함수를 (빠르게) 실행하는 문제
"""
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
"""
# 미리 w(0,0,0) ~ w(20,20,20) 까지 계산해놓고 그에 맞는거 출력
import sys
w = [[[0 for col in range(21)] for row in range(21)] for depth in range(21)]
for A in range(21) : 
    for B in range(21) : 
        for C in range(21) : 
            if A <= 0 or B <= 0 or C <= 0 : 
                w[A][B][C] = 1
            elif A < B < C : 
                w[A][B][C] = w[A][B][C-1] + w[A][B-1][C-1] - w[A][B-1][C]
            else : 
                w[A][B][C] = w[A-1][B][C] + w[A-1][B-1][C] + w[A-1][B][C-1] - w[A-1][B-1][C-1]

while 1 : 
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1 : 
        exit(0)
    print("w(%d, %d, %d) = " %(a, b, c), end="")
    if a <= 0 or b <= 0 or c <= 0 : 
        a = b = c = 0
    elif a > 20 or b > 20 or c > 20 : 
        a = b = c = 20
    print(w[a][b][c])