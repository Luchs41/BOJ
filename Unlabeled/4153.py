# BOJ 4153
# 세 수로 직각삼각형인지 아닌지 알아내기

while 1 : 
    a = list(map(int, input().split()))
    if a[0] == 0 : 
        break
    a.sort()
    if a[2]**2 == a[0]**2 + a[1]**2 : 
        print("right")
    else : 
        print("wrong")