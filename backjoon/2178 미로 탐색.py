import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

dist = [[0 for j in range(101)] for i in range(100)]
visited = [[0 for j in range(101)] for i in range(100)]

N, M = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# 상하좌우
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def BFS(r, c):
    queue = deque()
    dist[r][c] = 1
    visited[r][c] = 1  # visited
    queue.append((r, c))

    while queue:
        cr, cc = queue.popleft()

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            if graph[nr][nc] == 0:
                continue
            if visited[nr][nc] == 1:
                continue
            dist[nr][nc] = dist[cr][cc] + 1
            visited[nr][nc] = 1  # visited
            queue.append((nr, nc))

        print('Map'.center(20, '-'))
        for r in range(N):
            for c in range(M):
                print(graph[r][c], end=' ')
            print()
        print('-' * 20)
        print('Distance'.center(20, '-'))
        for r in range(N):
            for c in range(M):
                print(dist[r][c], end=' ')
            print()
        print('-' * 20)
        print('visited'.center(20, '-'))
        for r in range(N):
            for c in range(M):
                print(visited[r][c], end=' ')
            print()
        print('-' * 20)


BFS(0, 0)

print(dist[N-1][M-1])
