# BOJ 15649
# 1~N까지의 자연수로 길이가 M인 수열(중복 X)를 모두 구하는 문제. 
# 백트래킹 알고리즘으로, 리스트에 숫자를 하나씩 추가하며 조건에 부합하는지 확인한다. 
N, M = map(int, input().split())
li = []

def DFS() :
    if len(li) == M :
        print(' '.join(map(str, li)))
        return
    
    for i in range(1, N + 1) :
        if i not in li :
            li.append(i)
            DFS()
            li.pop()
DFS()