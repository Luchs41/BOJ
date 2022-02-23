# BOJ 2178
# 미로의 첫째 칸에서 마지막 칸으로 이동하는 최단경로의 길이를 출력하는 문제. (항상 도착위치로 이동할 수 있는 경우만 주어진다. )

N, M = map(int, input().split())
maze = []
for _ in range(N) : 
    maze.append(list(map(int, input())))
    