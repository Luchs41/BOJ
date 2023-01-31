# BOJ 1918
# 입력으로 들어오는 중위 표기식을 후위 표기식으로 바꾸어 출력
# 피연산자는 바로 출력
# 연산자는 우선순위에 따라 처리
# stack이 비어있다면 자신을 push
# stack top이 자신보다 우선순위가 낮을 때까지 pop(출력) 후 자신을 push
# 단, '('는 ')'가 아니면 pop 하지 않는다. 
# ')'가 나오면 '('가 나올 때까지 pop(출력)
# 문자열이 끝나면 stack이 빌 때까지 pop(출력)

import sys

addop = ['+', '-']
mulop = ['*', '/']

str_in = sys.stdin.readline().rstrip()
stack = []
result = str()

for char in str_in : 
  if char.isalpha() == True : 
    result += char
  else : 
    if char == '(' : # '('보다 우선순위가 높은 연산자는 없으므로 바로 push
      stack.append(char)
    elif char in mulop : 
      while stack and stack[-1] in mulop : 
        result += stack.pop()
      stack.append(char)
    elif char in addop : # addop보다 우선순위가 낮은 연산자는 없으므로, 특수 케이스인 '('만 아니라면 모두 pop 후 push
      while stack and stack[-1] != '(' : 
        result += stack.pop()
      stack.append(char)
    elif char == ')' : 
      while stack and stack[-1] != '(' : 
        result += stack.pop()
      stack.pop()

while stack : 
  result += stack.pop()
print(result)
