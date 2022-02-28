# BOJ 10828
# 기본적인 스택을 구현하는 문제
# 첫 줄에 명령의 수 N이 주어지고, 이후 N개의 줄에 명령어가 주어진다. 
import sys
from collections import deque
N = int(input())
stack = deque()
for _ in range(N) : 
    command = list(sys.stdin.readline().split())
    if len(command) == 2 : 
        command[1] = int(command[1])
    
    if command[0] == 'push' : 
        stack.append(command[1])
    if command[0] == 'pop' : 
        if len(stack) == 0 : 
            print('-1')
        else : 
            print(stack.pop())
    if command[0] == 'top' : 
        if len(stack) == 0 : 
            print('-1')
        else : 
            print(stack[len(stack) - 1])
    if command[0] == 'size' : 
        print(len(stack))
    if command[0] == 'empty' : 
        if len(stack) == 0 : 
            print('1')
        else : 
            print('0')