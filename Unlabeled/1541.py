# BOJ 1541
# 잃어버린 괄호
# 양수와 +, -로 구성된 식에 적절히 괄호를 배치하여 식의 값이 최소가 되는 프로그램을 작성하시오. 
# 가장 처음과 마지막 문자는 숫자. 5자리 이상의 숫자는 없고, 수는 0으로 시작할 수 있다. 
# ex) 55-50+40 -> -35

a = input().split('-')
numbers = list()
for i in a : 
  _sum = 0
  poly = i.split('+')
  for j in poly : 
    _sum += int(j)
  numbers.append(_sum)
result = numbers[0]
for i in range(1, len(numbers)) : 
  result -= numbers[i]
print(result)
