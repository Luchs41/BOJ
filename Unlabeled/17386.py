# BOJ 17386
# 선분 교차 1
# 2차원 좌표 평면 위의 두 선분이 교차하는지 아닌지 구해보자

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def ccw(x1, y1, x2, y2, x3, y3) : 
  op = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
  if op > 0 : 
    return 1
  elif op < 0 : 
    return -1
  else : 
    return 0
  
if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) < 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) < 0 : 
  result = 1
else : 
  result = 0

print(result)
