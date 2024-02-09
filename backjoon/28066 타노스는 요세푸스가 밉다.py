import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

que = deque([i for i in range(1, N+1)])
# print(que)

while que:
    first = que.popleft()
    que.append(first)
    if len(que) >= K:
        for i in range(K - 1):
            last = que.popleft()
    else:
        for i in range(len(que)):
            last = que.popleft()
print(last)
