import sys

sys.stdin = open('input.txt', 'r')

K, N = map(int, sys.stdin.readline().split())
lans = []

for i in range(K):
    lans.append(int(sys.stdin.readline()))

lans.sort()

right = lans[-1]
left = 1

res = 0
while left <= right:
    mid = (left + right) // 2
    print(mid)
    cnt = 0
    for lan in lans:
        cnt += lan // mid
    if cnt < N:
        right = mid - 1
    else:
        left = mid + 1
        if mid > res:
            res = mid

print(res)