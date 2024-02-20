import sys

sys.stdin = open('input.txt', 'r')

INF = int(1e9)

n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
items.insert(0, 0)

dist_map = [[INF for j in range(n + 1)] for i in range(n + 1)]

for i in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    dist_map[a][b] = l
    dist_map[b][a] = l

for i in range(1, len(dist_map)):
    dist_map[i][i] = 0

# for i in range(1, len(graph)):
#     for j in range(1, len(graph)):
#         print(dist_map[i][j], end=' ')
#     print()

for k in range(1, len(dist_map)):
    for i in range(1, len(dist_map)):
        for j in range(1, len(dist_map)):
            if dist_map[i][j] > dist_map[i][k] + dist_map[k][j]:
                dist_map[i][j] = dist_map[i][k] + dist_map[k][j]

# for i in range(1, len(graph)):
#     for j in range(1, len(graph)):
#         print(dist_map[i][j], end=' ')
#     print()

result = [0 for i in range(n + 1)]
for i in range(1, len(dist_map)):
    for j in range(1, len(dist_map)):
        if dist_map[i][j] <= m:
            result[i] += items[j]

# print(result)
print(max(result))