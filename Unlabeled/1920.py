# BOJ 1920
# N개의 정수 A[1]~A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내라
# 자연수 N, N개의 정수 A[1]~A[N], 자연수 M, M개의 수가 주어진다. 
# M개의 수가 A 안에 존재하는지 알아내어 존재하면 1을, 존재하지 않으면 0을 출력
# 이분탐색 안하고 i in B => 이렇게하면 시간초과
import sys
N = int(input())
A = list(map(int,sys.stdin.readline().split()))

M = int(input())
B = list(map(int,sys.stdin.readline().split()))

A.sort()

for i in B : 
    left = 0
    right = N - 1
    mid = int((left + right) / 2)
    flag = 0
    while right-left >= 0 : 
        if A[mid] == i : 
            flag = 1
            break
        elif A[mid] < i : 
            left = mid + 1
        else : 
            right = mid - 1
        mid = int((left + right) / 2)
    print(flag)