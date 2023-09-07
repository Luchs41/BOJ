# BOJ 4659
# 비밀번호 발음하기
# 모음 하나 반드시 포함
# 모음이 3개 혹은 자음이 3개 오면 안됨
# 같은 글자가 연속으로 두번 오면 안됨(ee와 oo 제외)

import sys
from collections import deque
input = sys.stdin.readline

vowel = ['a', 'e', 'i', 'o', 'u']

while 1 : 
  password = input().rstrip()
  if password == 'end' : 
    break
  pwd = list(password)
  vowelFlag = False
  v_cnt = 0
  c_cnt = 0
  same = 0
  for i in range(len(pwd)) : 
    if i > 0 : 
      if pwd[i] == pwd[i - 1] : 
        if pwd[i] != 'e' and pwd[i] != 'o' : 
          same = 1
          break
    
    if pwd[i] in vowel : 
      vowelFlag = True
      v_cnt += 1
      c_cnt = 0
      if v_cnt == 3 : 
        same = 1
        break
    else : 
      v_cnt = 0
      c_cnt += 1
      if c_cnt == 3 : 
        same = 1
        break
  
  if same != 1 and vowelFlag == True : 
    print("<" + password + "> is acceptable.")
  else : 
    print("<" + password + "> is not acceptable.")
    
