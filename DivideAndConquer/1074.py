# BOJ 1074
# 2^N X 2^N 크기인 2차원 배열을 Z 모양으로 탐색
# N, r, c가 주어지면, r행 c열을 몇 번째로 방문했는지 출력한다. 

N, r, c = map(int, input().split())
result = 0
while N > 0 : 
    N -= 1
    div = 2 ** N
    if r >= div and c >= div : 
        result += (div ** 2) * 3
        r -= div
        c -= div
    elif r >= div and c < div : 
        result += (div ** 2) * 2
        r -= div
    elif r < div and c >= div : 
        result += (div ** 2)
        c -= div
    else : 
        result += 0

print(result)