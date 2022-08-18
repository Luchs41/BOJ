# BOJ 10250
# 직사각형 모양 호텔, 각 층에 W개의 방이 있는 H층 건물
# 호수는 (Y)YXX (ex : 1202)식으로
# 엘레베이터는 YY01호 옆에있고 손님들은 엘베 앞 선호(층은 낮을수록 선호)
# H, W, N순으로 주어지며 H*W호텔의 N번째 손님이 몇호에 배정받는지 출력

case = int(input())
for i in range(case) : 
    H, W, N = map(int, input().split())
    y = N // H + 1
    x = N % H
    if x == 0 : 
        x = H
        y -= 1
    print(x * 100 + y)