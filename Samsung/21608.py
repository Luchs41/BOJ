# BOJ 21608
# 상어 초등학교

# 현재 자리와 앉을 학생이 주어졌을 때, 각 자리 별 만족도를 계산하는 함수
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def find(cur_s):
  check[cur_s] = True
  s = []
  for i in range(n): 
    for j in range(n):
      if seat[i][j] != 0:
        continue
      empty = 0
      fav = 0
      for k in range(4): 
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
          if seat[nx][ny] == 0:
            empty += 1
          elif seat[nx][ny] in p[cur_s]:
            fav += 1
      res = [fav, empty, i, j]
      s.append(res)
  s = sorted(s, key=lambda x : (-x[0], -x[1], x[2], x[3]))
  return (s[0][2], s[0][3])
  
# 전체 학생의 만족도를 계산하는 함수
def cal():
  ans = 0
  for i in range(n):
    for j in range(n):
      cur = seat[i][j]
      temp = 0
      for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n and 0 <= ny < n and seat[nx][ny] in p[cur]:
          temp += 1
      if temp != 0:
        ans += 10 ** (temp-1)
  return ans
  

n = int(input())
p = [[0] * 4 for i in range(n*n + 1)]
seat = [[0] * n for _ in range(n)]
check = [False] * (n*n + 1)
order = []

for _ in range(n*n): 
  line = list(map(int, input().split()))
  stu = line[0]
  order.append(stu)
  like = line[1:]
  for i in range(4): 
    p[stu][i] = like[i]

for c in order:
  temp = find(c)
  seat[temp[0]][temp[1]] = c

print(cal())