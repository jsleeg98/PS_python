import sys
import heapq

sys.stdin = open('input.txt', 'r')

pos = []
graph = [[] for i in range(10001)]
N, D = map(int, sys.stdin.readline().split())
for i in range(N):
    s, e, d = map(int, sys.stdin.readline().split())
    pos.append(s)
    pos.append(e)
    if e - s > d and e <= D:
        graph[s].append((e, d))


pos = list(set(pos))
pos.sort()

# print(pos)

for i in range(len(pos)):
    graph[pos[i]].append((D, D-pos[i]))
    for j in range(i+1, len(pos)):
        graph[pos[i]].append((pos[j], pos[j]-pos[i]))

if len(graph[0]) == 0:
    for i in pos:
        graph[0].append((i, i))

# for i in range(len(graph)):
#     if len(graph[i]) != 0:
#         print(f'{i} : {graph[i]}')

INF = int(1e9)
def dijkstra(start):
    distances = [INF for i in range(10001)]
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for g in graph[now]:
            cost = dist + g[1]
            if distances[g[0]] > cost:
                distances[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))

    return distances

distances = dijkstra(0)
# print(distances[50])
# print(distances[100])
print(distances[D])
