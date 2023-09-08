# BOJ 14444(BOJ 13275와 동일)
# 가장 긴 팰린드롬 부분 문자열
# 주어진 문자열 S의 부분문자열 중 팰린드롬 이면서 길이가 가장 긴 것의 길이를 구하는 프로그램
# Manacher 알고리즘 -> 문자열의 부분 문자열 중 팰린드롬인것 중 가장 긴 것의 길이를 구하는 알고리즘에 최적화
# 시간복잡도 O(n)
# https://edder773.tistory.com/178

def manachers(S, N) : 
  A = [0] * N
  r, p = 0, 0
  for i in range(N) : 
    if i <= r : 
      A[i] = min(A[2 * p - i], r - i)
    while i - A[i] - 1 >= 0 and i + A[i] + 1 < N and S[i - A[i] - 1] == S[i + A[i] + 1] : 
      A[i] += 1
    if r < i + A[i] : 
      r = i + A[i]
      p = i
  return A

S = input()
N = len(S)
s = ""

for i in range(N) : 
  s += '#'
  s += S[i]
s += '#'

A = manachers(s, len(s))
print(max(A))