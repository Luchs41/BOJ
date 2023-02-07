# BOJ 1941
# 회의실 배정
# 회의를 1. 종료시간 2. 시작시간의 오름차순으로 정렬
# 그 후 겹치지 않게 하나씩 선택
import sys

input = sys.stdin.readline
N = int(input())
timeTable = list()
for _ in range(N) : 
  start, end = map(int, input().split())
  timeTable.append([start, end])
timeTable.sort(key = lambda x : (x[1], x[0]))


curStart, curEnd = -1, -1
count = 0
for meeting in timeTable : 
  if meeting[0] >= curEnd : 
    count += 1
    curStart = meeting[0]
    curEnd = meeting[1]
print(count)

