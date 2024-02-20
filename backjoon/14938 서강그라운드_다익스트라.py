import sys
import heapq

sys.stdin = open('input.txt', 'r')

INF = int(1e9)

n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
items.insert(0, 0)

graph = [[] for i in range(n + 1)]

for i in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

for i in range(1, len(graph)):
    graph[i].append((i, 0))

def dijkstra(start):
    distances = [INF for i in range(n + 1)]
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for g in graph[now]:
            cost = g[1] + dist
            if cost < distances[g[0]]:
                distances[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))

    return distances

result = [0 for i in range(len(graph))]
final_result = 0
for i in range(1, len(graph)):
    distances = dijkstra(i)
    for j in range(1, len(graph)):
        if distances[j] <= m:
            result[i] += items[j]
    if result[i] > final_result:
        final_result = result[i]
# print(max(result))
print(final_result)