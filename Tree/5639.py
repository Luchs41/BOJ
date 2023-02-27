# BOJ 5639
# Binary Search Tree
# 입력 : BST를 전위 순회한 결과
# 출력 : BST를 후위 순회한 결과

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
tree = []
while 1 : 
  try : 
    num = int(input())
    tree.append(num)
  except : 
    break
def postorder(start, end) : 
  if start > end : 
    return
  
  mid = end + 1
  for i in range(start + 1, end + 1) : 
    if tree[start] < tree[i] : 
      mid = i
      break
  postorder(start + 1, mid - 1)
  postorder(mid, end)
  print(tree[start])

postorder(0, len(tree) - 1)