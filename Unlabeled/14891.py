# BOJ 14891
from collections import deque
import sys
saw = [0, 0, 0, 0]
saw[0] = deque(input())
saw[0] = deque(map(int, saw[0]))
saw[1] = deque(input())
saw[1] = deque(map(int, saw[1]))
saw[2] = deque(input())
saw[2] = deque(map(int, saw[2]))
saw[3] = deque(input())
saw[3] = deque(map(int, saw[3]))

def rotate(s, direction) : 
    if direction == 1 : 
        s.appendleft(s.pop())
    elif direction == -1 : 
        s.append(s.popleft())


k = int(input())
def check(saw, sawdir, picsaw, picdir) : 
    sawdir[picsaw] = picdir
    for i in range(picsaw, 3) : 
        if saw[i][2] != saw[i + 1][6] : 
            sawdir[i + 1] = sawdir[i] * -1
        else : 
            break
    for i in range(picsaw, 0, -1) : 
        if saw[i][6] != saw[i - 1][2] : 
            sawdir[i - 1] = sawdir[i] * -1
        else : 
            break
for n in range(k) : 
    sawdir = [0, 0, 0, 0]
    rotsaw, rotdir = map(int, input().split())
    rotsaw -= 1
    check(saw, sawdir, rotsaw, rotdir)
    for i in range(4) : 
        rotate(saw[i], sawdir[i])
result = 0
for i in range(4) : 
    if saw[i][0] == 1 : 
        result += 2 ** i
print(result)
