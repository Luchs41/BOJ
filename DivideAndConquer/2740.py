# BOJ 2740
# N*M 크기의 행렬 A와 M*K 크기의 행렬 B의 곱을 구하는 프로그램
# 첫째 줄에 행렬 A의 크기 N과 M이 주어지고, 다음 N개 줄에 행렬 A의 원소 M개가 순서대로 주어진다. 이어서 행렬 B의 크기 M과 K가 주어지고 이어서 M개의 줄에 행렬 B의 원소 K개가 차례대로 주어진다. 
import sys
N, M = map(int, input().split())
matA = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

M, K = map(int, input().split())
matB = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
matC = [[0]*K for i in range(N)]


for i in range(N) : 
    for j in range(K) : 
        for k in range(M) : 
            matC[i][j] += matA[i][k] * matB[k][j]
for i in matC : 
    for j in i : 
        print(j, end=' ')
    print()