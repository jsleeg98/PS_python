import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

li = []
for _ in range(N):
    x, y = map(int, input().split())
    li.append([x, y])

ans = []
for i in range(len(li)):
    cri = li[i]
    cnt = 0
    for j in range(len(li)):
        if li[j][0] > li[i][0] and li[j][1] > li[i][1]:
            cnt += 1
    ans.append(cnt + 1)

for i in ans:
    print(i, end=' ')