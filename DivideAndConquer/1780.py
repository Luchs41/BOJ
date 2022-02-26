# BOJ 1780
# BOJ 2630번 문제와 비슷하나, 3가지의 색깔로 나뉘고 종이를 3등분으로 조집니다. 

import sys
count = [0, 0, 0]
def check(x, y, N) : 
    global count
    first = mat[x][y]
    unit = N // 3
    for i in range(x, x + N) : 
        for j in range(y, y + N) : 
            if mat[i][j] != first :
                for nx in (0, 1, 2) : 
                    for ny in (0, 1, 2) : 
                        check(x + nx * unit, y + ny * unit, unit)
                return 
    count[first] += 1
N = int(input())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check(0, 0, N)
print(count[-1])
print(count[0])
print(count[1])