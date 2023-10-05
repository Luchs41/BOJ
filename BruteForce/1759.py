# BOJ 1759
vowel = ['a', 'e', 'i', 'o', 'u']
def go(n, alpha, password, i) : 
  if len(password) == n :
    if check(password) : 
      print(password)
    return
  if i >= len(alpha) : 
    return
  go(n, alpha, password + alpha[i], i + 1)
  go(n, alpha, password, i + 1)

def check(password) : 
  ja = 0
  mo = 0
  for i in password : 
    if i in vowel : 
      mo += 1
    else : 
      ja += 1
  return ja >= 2 and mo >= 1



l, c = map(int, input().split())
a = list(input().split())
a.sort()

go(l, a, '', 0)