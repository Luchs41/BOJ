# BOJ 1105
# 팔
# L이상 R이하 중 8이 가장 적게 들어있는 수에 들어있는 8의 개수를 구하는 프로그램


L, R = input().split()

answer = 0

if len(L) != len(R) : 
  print(answer)
else : 
  for i in range(len(L)) : 
    if L[i] == R[i] :
      if L[i] == '8' : 
        answer += 1
    else : 
      break
  
  print(answer)

