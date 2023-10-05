# BOJ 17427
# 배수를 이용해서 계산

n = int(input())
answer = 0
for i in range(1, n+1) : 
  answer += i * (n // i)
print(answer)