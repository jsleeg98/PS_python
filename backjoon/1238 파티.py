import sys
import heapq

INF = int(1e9)
sys.stdin = open('input.txt', 'r')

N, M, X = map(int, input().split())

graph = [[] for i in range(N+1)]



for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))

def dijkstra(start):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

distances = [[]]

for i in range(1, N+1):
    distances.append(dijkstra(i))

res = []
for i in range(1, N+1):
    res.append(distances[i][X] + distances[X][i])

print(max(res))
