import sys
import heapq

INF = int(1e9)
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n + 1)]

for i in range(n - 1):
    p, c, d = map(int, input().split())
    graph[p].append((c, d))
    graph[c].append((p, d))

def dijkstra(start):
    distances = [INF for i in range(n + 1)]
    distances[start] = 0
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

if n == 1:
    print(0)
else:
    distances = dijkstra(1)
    max_dist = 0
    new_start = 0
    for i in range(1, n + 1):
        if max_dist < distances[i]:
            max_dist = distances[i]
            new_start = i
    new_distances = dijkstra(new_start)
    print(max(new_distances[1:]))
