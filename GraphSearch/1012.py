# BOJ 1012
# 첫 줄에 테스트 케이스의 수 / 각 테스트 케이스의 첫째 줄에 배추밭의 가로, 세로 길이와 배추의 수가 주어지고, 다음 줄에는 배추의 위치가 주어진다. 
# 2667번 문제처럼 몇 개의 단위로 이루어졌는지 구하면 된다. 

from collections import deque
def BFS(graph, a, b) : 
    queue = deque()
    Xboarder = len(graph)
    Yboarder = len(graph[0])
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue : 
        x, y = queue.popleft()
        if x - 1 >= 0 :
            if graph[x - 1][y] == 1 : 
                graph[x - 1][y] = 0
                count += 1
                queue.append((x-1, y))
        if x + 1 < Xboarder : 
            if graph[x + 1][y] == 1 : 
                graph[x + 1][y] = 0
                count += 1
                queue.append((x+1,y))
        if y - 1 >= 0 : 
            if graph[x][y - 1] == 1 : 
                graph[x][y - 1] = 0
                count += 1
                queue.append((x, y - 1))
        if y + 1 < Yboarder :
            if graph[x][y + 1] == 1 :
                graph[x][y + 1] = 0
                count += 1
                queue.append((x, y + 1))
        
    return count
tc = int(input())
for _ in range(tc) : 
    graph = []
    width, height, baechu = map(int, input().split())
    for i in range(width) : 
        graph.append([0 for __ in range(height)])
    
    for i in range(baechu) : 
        inx, iny = map(int, input().split())
        graph[inx][iny] = 1
    worm = []
    for i in range(width) : 
        for j in range(height) : 
            if graph[i][j] == 1 : 
                worm.append(BFS(graph, i, j))
    print(len(worm))

    