import sys

sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())

edges = []

parent = [0] * (V + 1)
for i in range(1, V + 1):
    parent[i] = i

for i in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
