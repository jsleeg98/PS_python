import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

N = int(input())
m = []
for i in range(N):
    tmp = input()
    m.append(tmp)


dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]
visit = [[0 for i in range(N)] for j in range(N)]
def bfs(r, c, color):
    cnt = 0
    q = deque()
    visit[r][c] = color
    q.append([r, c])
    while q:
        cnt += 1
        cr, cc = q.popleft()
        for i in range(4):
            nr = cr + dir_r[i]
            nc = cc + dir_c[i]
            if 0 <= nr < N and 0 <= nc < N:
                if m[nr][nc] == '1' and visit[nr][nc] == 0:
                    q.append([nr, nc])
                    visit[nr][nc] = color

    return cnt

results = []
color = 1
for r in range(N):
    for c in range(N):
        if m[r][c] == '1' and visit[r][c] == 0:
            results.append(bfs(r, c, color))
            color += 1

results.sort()
print(len(results))
for i in range(len(results)):
    print(results[i])

# for r in range(N):
#     for c in range(N):
#         print(visit[r][c], end=' ')
#     print()
