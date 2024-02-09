import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

N = int(input())
M = int(input())

visit = [0 for i in range(N+1)]
link = [[] for i in range(N+1)]


for i in range(M):
    s, e = map(int, input().split())
    link[s].append(e)
    link[e].append(s)

def bfs(node):
    cnt = 0
    que = deque()
    que.append(node)
    visit[node] = 1
    while que:
        cnt += 1
        s = que.popleft()
        # print(s)
        for n in link[s]:
            if visit[n] == 0:
                que.append(n)
                visit[n] = 1

    return cnt

print(bfs(1)-1)

