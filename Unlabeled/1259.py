# BOJ 1259
# 팰린드롬수인지 아닌지 확인하여 yes / no 출력

pelin = input()
while pelin != '0' : 
    if pelin == ''.join(reversed(pelin)) : 
        print("yes")
    else : 
        print("no")
    pelin = input()