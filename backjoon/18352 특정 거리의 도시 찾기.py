import sys
import heapq

sys.stdin = open('input.txt', 'r')

N, M, K, X = map(int, sys.stdin.readline().split())
INF = int(1e9)

graph = [[] for i in range(N + 1)]

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append((e, 1))

def dijkstra(start):
    distances = [INF for i in range(N + 1)]
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distances[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distances

distances = dijkstra(X)
res = []
for i, d in enumerate(distances):
    if d == K:
        res.append(i)

if len(res) > 0:
    res.sort()
    for i in res:
        print(i)
else:
    print(-1)