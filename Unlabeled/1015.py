# BOJ 1015
# 주어진 수 N과 배열 A를 이용, 배열 A에 수열 P를 적용한 결과가 비내림차순이 되는 수열 P를 찾는다. 
# 적용 : B[P[i]] = A[i], B는 적용 결과

N = int(input())
A = list(map(int,input().split()))
sortedA = sorted(A)
#print(A, sortedA)
P = [-1]*N
for i in range(N) : 
    idx = sortedA.index(A[i])
    sortedA[idx] = -2
    P[i] = idx
    

for i in P : 
    print(i, end=" ")
print()