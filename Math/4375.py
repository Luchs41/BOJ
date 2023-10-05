# BOJ 4375
# 2와 5로 나누어 떨어지지 않는 정수 n이 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오

while True : 
  try : 
    n = int(input())
  except : 
    break
  num = 0
  i = 1
  while True : 
    num = num * 10 + 1
    num %= n
    if num == 0 : 
      print(i)
      break
    i += 1