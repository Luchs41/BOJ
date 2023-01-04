# BOJ 1676
# N!이 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지의 0의 개수를 구하는 문제
# 1~N까지의 수를 check 함수로 check
# check 함수는 2와 5의 거듭제곱에 대한 소인수를 검사
# 세제곱까지만 하는 이유는 어차피 2와 5가 짝지어 있어야 뒤에 0이 붙는데, 
# 5^3 = 125로 5^4부터는 500을 넘어가기 때문
N = int(input())
count2 = 0
count5 = 0
def check2(num) : 
    global count2
    if num % 2 == 0 : 
        count2 += 1
        if num // 2 % 2 == 0 : 
            count2 += 1
            if num // 2 // 2 % 2 == 0 : 
                count2 += 1
    
def check5(num) : 
    global count5
    if num % 5 == 0 : 
        count5 += 1
        if num // 5 % 5 == 0 : 
            count5 += 1
            if num // 5 // 5 % 5 == 0 : 
                count5 += 1

for i in range(1, N + 1) : 
    check2(i)
    check5(i)
print(min(count2, count5))