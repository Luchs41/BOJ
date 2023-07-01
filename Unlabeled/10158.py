# BOJ 10158
# 개미
# 가로 w, 세로 h인 2차원 격자에서 개미는 (p, q)에서 시작
# 개미는 한시간 후 (p+1, q+1)로 이동 -> 45도 이동, 경계면에 부딪치면 반사되어서 이동
# w, h, p, q, 시간 t가 주어질 때, t 시간 후 개미의 위치 좌표 (x, y)를 출력한다. 
# t가 200,000,000 까지이므로 그냥 반복문 돌리면 시간초과

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = (p + t) // w
y = (q + t) // h
if x % 2 == 0 : 
    x = (p + t) % w
else : 
    x = w - (p + t) % w

if y % 2 == 0 : 
    y = (q + t) % h
else : 
    y = h - (q + t) % h
print(x, y)
