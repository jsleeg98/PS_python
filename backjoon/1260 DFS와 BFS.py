import sys
import queue

sys.stdin = open('input.txt', 'r')

N, M, V = map(int, sys.stdin.readline().split())
visited = [0 for i in range(N + 1)]
vertex = [[] for i in range(N + 1)]

dfs_result = []

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    vertex[s].append(e)
    vertex[e].append(s)

for i in range(N):
    vertex[i+1].sort()

def dfs(v):
    if visited[v] == 1:
        return
    dfs_result.append(v)
    visited[v] = 1
    for i in vertex[v]:
        dfs(i)

dfs(V)

visited = [0 for i in range(N + 1)]

q=queue.Queue()

bfs_result = []

def bfs(start):
    bfs_result.append(start)
    visited[start] = 1
    q.put(start)
    while not q.empty():
        v = q.get()
        for i in vertex[v]:
            if visited[i] == 0:
                visited[i] = 1
                q.put(i)
                bfs_result.append(i)

bfs(V)

for i in dfs_result:
    print(i, end=' ')
print()
for i in bfs_result:
    print(i, end=' ')
