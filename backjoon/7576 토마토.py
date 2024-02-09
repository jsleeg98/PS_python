import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

C, R = map(int, input().split())

m = []

ripe = deque()
unripe = 0
for r in range(R):
    tmp = list(map(int, input().split()))
    m.append(tmp)
    for c in range(C):
        if tmp[c] == 1:
            ripe.append([r, c])
        elif tmp[c] == 0:
            unripe += 1

dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]
def bfs(ripe):
    global unripe
    next_ripe = deque()
    while ripe:
        cr, cc = ripe.popleft()
        for i in range(4):
            nr = cr + dir_r[i]
            nc = cc + dir_c[i]
            if 0 <= nr < R and 0 <= nc < C:
                if m[nr][nc] == 0:
                    next_ripe.append([nr, nc])
                    m[nr][nc] = 1
                    unripe -= 1
    return next_ripe

cnt = -1
while ripe:
    ripe = bfs(ripe)
    for r in range(R):
        for c in range(C):
            print(m[r][c], end=' ')
        print()
    print('-' * 20)
    cnt += 1

if unripe == 0:
    print(cnt)
else:
    print(-1)