# BOJ 14891
# 네개의 이웃한 톱니바퀴 중 K번만큼 하나의 톱니를 돌린다. 
# 각 톱니는 자석으로 되어있어서 인접한 톱니가 서로 다른 극(N + S)이면 걘 반대로 돌아간다. 
# K번만큼 돌리고 난 후 각 톱니의 12시 방향의 톱니가 S극이면 점수 추가(2의 거듭제곱 순), 최종적으로 점수를 출력해라
# 구현 : 하라는대로 함. 
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
