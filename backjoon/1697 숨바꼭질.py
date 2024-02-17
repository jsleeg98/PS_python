import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

N, K = map(int, sys.stdin.readline().split())

q = deque()

visit = [0 for i in range(100001)]

q.append((N, 0))
visit[N] = 1

while q:
    now, sec = q.popleft()
    if now == K:
        print(sec)
        break
    if now + 1 <= 100000:
        if visit[now + 1] == 0:
            q.append(((now + 1), sec + 1))
            visit[now + 1] = 1
    if now - 1 >= 0:
        if visit[now - 1] == 0:
            q.append(((now - 1), sec + 1))
            visit[now - 1] = 1
    if now * 2 <= 100000:
        if visit[now * 2] == 0:
            q.append(((now * 2), sec + 1))
            visit[now * 2] = 1
