import copy
import sys
from functools import cmp_to_key
from collections import deque
import heapq

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline


class Rabbit:
    def __init__(self, r, c, pid, d):
        self.r = r
        self.c = c
        self.pid = pid
        self.d = d
        self.jump = 0
        self.score = 0

    # 이동할 토끼를 결정하기 위해 정렬함수를 만들어줍니다.
    def __lt__(self, other):
        if self.jump != other.j:
            return self.jump < other.j
        if self.r + self.c != other.r + other.c:
            return self.r + self.c < other.r + other.c
        if self.r != other.r:
            return self.r < other.r
        if self.c != other.c:
            return self.c < other.c
        return self.pid < other.pid


def comparator_move(a, b):
    if a.jump < b.jump:
        return -1
    elif a.jump == b.jump:
        if a.r + a.c < b.r + b.c:
            return -1
        elif a.r + a.c == b.r + b.c:
            if a.r < b.r:
                return -1
            elif a.r == b.r:
                if a.c < b.c:
                    return -1
                elif a.c == b.c:
                    if a.pid < b.pid:
                        return -1
                    else:
                        return 1
                else:
                    return 1
            else:
                return 1
        else:
            return 1
    else:
        return 1


def comparator_loc(a, b):
    if a[0] + a[1] > b[0] + b[1]:
        return -1
    elif a[0] + a[1] == b[0] + b[1]:
        if a[0] > b[0]:
            return -1
        elif a[0] == b[0]:
            if a[1] > b[1]:
                return -1
            else:
                return 1
        else:
            return 1
    else:
        return 1

def comparator_after_K(a, b):
    if a.r + a.c > b.r + b.c:
        return -1
    elif a.r + a.c == b.r + b.c:
        if a.r > b.r:
            return -1
        elif a.r == b.r:
            if a.c > b.c:
                return -1
            elif a.c == b.c:
                if a.pid > b.pid:
                    return -1
                else:
                    return 1
            else:
                return 1
        else:
            return 1
    else:
        return 1


def print_rabbit(rabbits):  # rabbits 출력
    for rabbit in rabbits.values():
        print(f'pid : {rabbit.pid}')
        print(f'r : {rabbit.r}')
        print(f'c : {rabbit.c}')
        print(f'd : {rabbit.d}')
        print(f'jump : {rabbit.jump}')
        print(f'score : {rabbit.score}')
        print('-' * 20)
    print('=' * 20)

def select_move(rabbit, N, M):
    # 위치 저장
    loc = []
    # 이동 거리 조정
    d_r = rabbit.d % ((N - 1) * 2)
    d_c = rabbit.d % ((M - 1) * 2)
    # 상
    tmp_r = rabbit.r - d_r
    if tmp_r < 1:
        tmp_d = 1 - tmp_r
        tmp_r = 1 + tmp_d
        if tmp_r > N:
            tmp_d = tmp_r - N
            tmp_r = N - tmp_d
    loc.append((tmp_r, rabbit.c))
    # 하
    tmp_r = rabbit.r + d_r
    if tmp_r > N:
        tmp_d = tmp_r - N
        tmp_r = N - tmp_d
        if tmp_r < 1:
            tmp_d = 1 - tmp_r
            tmp_r = 1 + tmp_d
    loc.append((tmp_r, rabbit.c))
    # 좌
    tmp_c = rabbit.c - d_c
    if tmp_c < 1:
        tmp_d = 1 - tmp_c
        tmp_c = 1 + tmp_d
        if tmp_c > M:
            tmp_d = tmp_c - M
            tmp_c = M - tmp_d
    loc.append((rabbit.r, tmp_c))
    # 우
    tmp_c = rabbit.c + d_c
    if tmp_c > M:
        tmp_d = tmp_c - M
        tmp_c = M - tmp_d
        if tmp_c < 1:
            tmp_d = 1 - tmp_c
            tmp_c = 1 + tmp_d
    loc.append((rabbit.r, tmp_c))
    # print(loc)
    loc.sort(key=cmp_to_key(comparator_loc))
    # print(loc)
    return loc[0]


# 입력 받기
rabbits = {}
T = int(input())
for _ in range(T):
    cmd = list(map(int, input().split()))
    if cmd[0] == 100:
        N = cmd[1]
        M = cmd[2]
        P = cmd[3]
        for i in range(4, 4 + 2 * P, 2):
            tmp_pid = cmd[i]
            tmp_d = cmd[i + 1]
            rabbits[tmp_pid] = Rabbit(1, 1, tmp_pid, tmp_d)
    elif cmd[0] == 200:  # 경주 진행
        K = cmd[1]
        S = cmd[2]
        set_move_pid = set()
        rabbit_pq = []

        for rabbit in rabbits.values():
            heapq.heappush(rabbit_pq, rabbit)

        for _ in range(K):
            # print_rabbit(rabbits)
            # 토끼 선정
            cur_rabbit = heapq.heappop(rabbit_pq)


            # max_jump = 4000000
            # tmp_rabbits = []
            # for rabbit in rabbits.values():
            #     if max_jump > rabbit.jump:
            #         tmp_rabbits = [rabbit]
            #         max_jump = rabbit.jump
            #     elif max_jump == rabbit.jump:
            #         tmp_rabbits.append(rabbit)
            # tmp_rabbits.sort(key=cmp_to_key(comparator_move))

            # 움직인 토끼 pid 저장
            move_pid = tmp_rabbits[0].pid
            set_move_pid.add(move_pid)
            # print(move_pid)
            # 이동 선택
            nr, nc = select_move(tmp_rabbits[0], N, M)
            # 이동
            rabbits[move_pid].r = nr
            rabbits[move_pid].c = nc
            rabbits[move_pid].jump += 1
            # 점수 산정
            for key in rabbits.keys():
                if key != move_pid:
                    rabbits[key].score += (nr + nc)
        # K턴 이후 최고 토끼 +S
        tmp_rabbits = []
        print(set_move_pid)
        for key in set_move_pid:
            tmp_rabbits.append(rabbits[key])
        tmp_rabbits.sort(key=cmp_to_key(comparator_after_K))
        rabbits[tmp_rabbits[0].pid].score += S
    elif cmd[0] == 300:  # 이동거리 변경
        pid = cmd[1]
        L = cmd[2]
        rabbits[pid].d *= L
    elif cmd[0] == 400:  # 최고 토끼 선정
        result = 0
        for rabbit in rabbits.values():
            if result < rabbit.score:
                result = rabbit.score
        print(result)
