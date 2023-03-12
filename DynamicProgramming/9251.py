# BOJ 9251
# LCS 구하기

a = ' ' + input()
b = ' ' + input()
LCS = [[0] * len(b) for _ in range(len(a))]

for i in range(1, len(a)) : 
  for j in range(1, len(b)) : 
    if a[i] == b[j] : 
      LCS[i][j] = LCS[i - 1][j - 1] + 1
    else : 
      LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
print(LCS[-1][-1])
