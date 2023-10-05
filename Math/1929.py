# BOJ 1929

M, N = map(int, input().split())

check = [0] * (N + 1)
check[0] = check[1] = True

for i in range(2, N + 1) : 
  if not check[i] : 
    j = i + i
    while j <= N : 
      check[j] = True
      j += i

for i in range(M, N + 1) : 
  if check[i] == False : 
    print(i)