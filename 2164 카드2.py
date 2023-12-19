import sys
import queue
from collections import deque

sys.stdin = open('input.txt', 'r')

N = int(input())
# que = queue.Queue()
que = deque()

for i in range(1, N+1):
    que.appendleft(i)

cnt = 0
while que:
    if len(que) == 1:
        break
    if cnt % 2 == 0:
        que.pop()
    else:
        tmp = que.pop()
        que.appendleft(tmp)
    cnt += 1

print(que.pop())
