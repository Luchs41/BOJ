# BOJ 19941
# 햄버거 분배
# 사람은 거리가 K 이하인 햄버거를 먹을 수 있다. 
# 0번부터 시작 기준 -> 최대한 자기 왼쪽거를 먹어야함
# 하나 먹으면 break 해야함


n, k = map(int, input().split())
table = list(input())
result = 0
for i in range(n) : 
  if table[i] == 'P' : 
    for j in range(max(i - k, 0), min(i + k + 1, n)) : 
      if table[j] == 'H' : 
        result += 1
        table[j] = ''
        break


print(result)