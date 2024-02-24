import sys

T = int(sys.stdin.readline())

for i in range(T):
    x, y, z = map(int, sys.stdin.readline().split())
    cnt = 0
    if x % 2 == 0:
        cnt += 1
    if y % 2 == 0:
        cnt += 1
    if z % 2 == 0:
        cnt += 1
    if cnt >= 2:
        print('R')
    else:
        print('B')
