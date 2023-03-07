# BOJ 1991
# 트리 순회
# 이진 트리를 입력받아 전위, 중위, 후위순회 한 결과를 출력
import sys
input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range(n) : 
  root, left, right = input().rstrip().split()
  tree[root] = [left, right]

def preorder(root) : 
  if root != '.' : 
    print(root, end="")
    preorder(tree[root][0])
    preorder(tree[root][1])

def inorder(root) : 
  if root != '.' : 
    inorder(tree[root][0])
    print(root, end="")
    inorder(tree[root][1])

def postorder(root) : 
  if root != '.' : 
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()