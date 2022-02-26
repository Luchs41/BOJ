# BOJ 2630
# 2^k * 2^k 크기의 종이의 각 칸에 파랑색 아니면 흰색으로 색칠이 되어있다. 
# 만약 종이의 모든 칸이 같은 색이면 내비둔다. 
# 다르다면 종이를 가로세로 절반으로 자른다. 위 과정을 반복하여 총 생기는 흰색 종이와 파란 종이의 개수를 출력한다. 
# 입력의 첫 줄에는 종이의 한 변의 길이가, 그 아래 줄에는 종이의 상태가 주어진다. 

import sys
count = [0, 0]

def check(x, y, N) : 
    global count
    global white, blue
    first = mat[x][y]
    for i in range(x, x + N) : 
        for j in range(y, y + N) : 
            if mat[i][j] != first :
                check(x, y, N // 2)
                check(x + N // 2, y, N // 2)
                check(x, y + N // 2, N // 2)
                check(x + N // 2, y + N // 2, N // 2)
                return 
    count[first] += 1
    
N = int(input())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check(0, 0, N)
print(count[0])
print(count[1])


