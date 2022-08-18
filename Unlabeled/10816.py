# BOJ 10816
# N개의 숫자 카드, 정수 M개가 주어졌을 때, 이 수가 적힌 숫자 카드가 몇 개 있는지 출력
import sys
from bisect import bisect_left, bisect_right
N = int(input())
cardList = list(map(int, sys.stdin.readline().split()))

M = int(input())
countList = list(map(int, sys.stdin.readline().split()))

cardList.sort()

for i in countList : 
    right = bisect_right(cardList, i)
    left = bisect_left(cardList, i)
    print(right - left, end = " ")
print()