import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
S = [0] * 21

M = int(input())

for _ in range(M):
    cmd = list(input().split())
    if cmd[0] == 'add':
        S[int(cmd[1])] = 1
    elif cmd[0] == 'check':
        if S[int(cmd[1])] == 1:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'remove':
        S[int(cmd[1])] = 0
    elif cmd[0] == 'toggle':
        S[int(cmd[1])] = (S[int(cmd[1])] + 1) % 2
    elif cmd[0] == 'all':
        S = [1] * 21
    elif cmd[0] == 'empty':
        S = [0] * 21

