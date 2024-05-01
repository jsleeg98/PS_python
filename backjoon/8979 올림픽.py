import sys
import heapq

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())

heap = []
for _ in range(N):
    i, G, S, C = map(int, input().split())
    heap.append((-G, -S, -C))
    if i == K:
        tmp = (-G, -S, -C)

heapq.heapify(heap)

cnt = 0
while True:
    top = heapq.heappop(heap)
    if tmp == top:
        break
    cnt += 1
print(cnt + 1)