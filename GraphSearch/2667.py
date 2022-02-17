# BOJ 2667
# 0과 1로 이루어진 2차원 배열을 입력받아, 1끼리 인접한 부분을 단지로 구분하여 총 단지의 수와 단지 내 1의 수를 출력한다. 

from collections import deque
def BFS(graph, a, b) : 
    queue = deque()
    boarder = len(graph)
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
        if x + 1 < boarder : 
            if graph[x + 1][y] == 1 : 
                graph[x + 1][y] = 0
                count += 1
                queue.append((x+1,y))
        if y - 1 >= 0 : 
            if graph[x][y - 1] == 1 : 
                graph[x][y - 1] = 0
                count += 1
                queue.append((x, y - 1))
        if y + 1 < boarder :
            if graph[x][y + 1] == 1 :
                graph[x][y + 1] = 0
                count += 1
                queue.append((x, y + 1))
        
    return count

        

N = int(input())
graph = []
for _ in range(N) :
    graph.append(list(map(int, input())))

danji = []
for i in range(N) : 
    for j in range(N) : 
        if graph[i][j] == 1:
            danji.append(BFS(graph, i, j))

danji.sort()
print(len(danji))
for i in danji : 
    print(i)