# BOJ 9012
# Check the given parenthesis string is valid or not
# The first line of the input, the number of test cases T is given. 
# The first line of each test case, there is a parentesis string which has length between 2 and 50. 

import sys
from collections import deque

T = int(input())
for _ in range(T) : 
    paren = sys.stdin.readline().strip()
    stack = deque()
    out = 'YES'
    for i in paren : 
        if i == "(" : 
            stack.append('(')
        elif i == ')' : 
            if len(stack) == 0 : 
                out = 'NO'
                break
            else : 
                stack.pop()
    if len(stack) != 0 : 
        out = 'NO'
    print(out)