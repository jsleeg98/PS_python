import sys

sys.stdin = open('input.txt', 'r')

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

# 거꾸로 찾아가지 않으면 최대 경우의 수 2^49 시간초과
flag = False
def DFS(cur, S):
    global flag
    if len(cur) == len(S):
        if cur == S:
            flag = True

    else:
        if cur[-1] == 'A':
            cur = cur[:-1]
            DFS(cur, S)
            cur += 'A'
        if cur[::-1][-1] == 'B':
            cur = cur[::-1][:-1]
            DFS(cur, S)

DFS(T, S)

if flag:
    print(1)
else:
    print(0)
