# BOJ 20920
# 영단어 암기
# 1. 자주 나오는 단어
# 2. 길이가 긴 단어
# 3. 사전순
# 우선순위로 정렬하되, 길이가 M 이상인 단어만 해당
# dictionary 활용 + 정렬 lambda 활용

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
wordList = dict()

for _ in range(n) : 
  word = input().rstrip()
  if len(word) < m : 
    continue
  else : 
    if word in wordList : 
      wordList[word] += 1
    else : 
      wordList[word] = 1

wordList = sorted(wordList.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))
for w in wordList : 
  print(w[0])