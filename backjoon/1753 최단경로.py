import sys
import heapq

sys.stdin = open('input.txt', 'r')

INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

linked_list = [[] for i in range(V + 1)]
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    linked_list[u].append((v, w))

def dijkstra(start):
    dist = [INF] * (V + 1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        d, s = heapq.heappop(q)
        if dist[s] < d:
            continue
        for i in linked_list[s]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dist

dist = dijkstra(K)

for d in dist[1:]:
    if d == int(1e9):
        print('INF')
    else:
        print(d)