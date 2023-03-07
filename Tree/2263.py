# BOJ 2263
# inorder와 postorder의 결과물로 preorder를 출력하기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

nodeNum = [0 for _ in range(n + 1)]
for i in range(n) : 
  nodeNum[inorder[i]] = i

def preorder(inStart, inEnd, postStart, postEnd) : 
  if (inStart > inEnd) or (postStart > postEnd) : 
    return
  
  root = postorder[postEnd]

  left = nodeNum[root] - inStart
  right = inEnd - nodeNum[root]

  print(root, end=" ")
  preorder(inStart, inStart + left - 1, postStart, postStart + left - 1)
  preorder(inEnd - right + 1, inEnd, postEnd - right, postEnd - 1)

preorder(0, n - 1, 0, n - 1)