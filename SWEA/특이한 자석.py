import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
magnets = None

def init_magnets():
    global magnets
    magnets = [[]]
    for _ in range(4):
        tmp = list(map(int, input().split()))
        magnets.append(deque(tmp))

def check(idx, d):
    global magnets
    dirs = [0, 0, 0, 0, 0]
    cur = idx
    cur_d = d
    dirs[cur] = d  # 방향 저장
    if cur < 4:
        flag = True
        # 오른쪽 방향 확인
        while True:
            mag1 = magnets[cur][2]
            mag2 = magnets[cur + 1][6]
            if mag1 != mag2:  # 도는 경우
                cur_d *= -1
                dirs[cur + 1] = cur_d
            else:  # 돌지 않는 경우
                flag = False

            cur += 1
            if cur > 3:
                break
            if not flag:
                break

    cur = idx
    cur_d = d
    if 1 < cur:
        flag = True
        # 왼쪽 방향 확인
        while True:
            mag1 = magnets[cur][6]
            mag2 = magnets[cur - 1][2]
            if mag1 != mag2:  # 도는 경우
                cur_d *= -1
                dirs[cur - 1] = cur_d
            else:  # 돌지 않는 경우
                flag = False
            cur -= 1
            if cur < 2:
                break
            if not flag:
                break

    return dirs

def rotate(dirs):
    global magnets
    for i in range(1, 5):
        if dirs[i] == 1:
            tmp = magnets[i].pop()
            magnets[i].appendleft(tmp)
        elif dirs[i] == -1:
            tmp = magnets[i].popleft()
            magnets[i].append(tmp)

def score(t):
    res = 0
    for i in range(1, 5):
        if magnets[i][0] == 1:
            res += 2 ** (i - 1)
    print(f'#{t} {res}')
    print()

T = int(input())
for t in range(1, T + 1):
    K = int(input())
    init_magnets()
    for _ in range(K):
        idx, d = map(int, input().split())
        dirs = check(idx, d)
        rotate(dirs)
    score(t)