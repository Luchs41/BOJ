# BOJ 1992
# 흰 점은 0, 검은 점은 1로 표시된 2차원 배열에서 0과 1을 묶어서 표현한다. 
# 첫 줄에는 2차원 배열(영상)의 크기 N이 주어진다(N = 2^k). 다음 줄부터는 영상의 정보가 주어진다. 

import sys
def check(x, y, N) : 
    
    first = mat[x][y]
    for i in range(x, x + N) : 
        for j in range(y, y + N) : 
            if mat[i][j] != first :
                print("(", end='')
                check(x, y, N // 2)
                check(x, y + N // 2, N // 2)
                check(x + N // 2, y, N // 2)
                check(x + N // 2, y + N // 2, N // 2)
                print(")", end='')
                return 
    print(first, end='')
    
N = int(input())
mat = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
check(0, 0, N)
print()