import copy
import sys
from functools import cmp_to_key
from collections import deque
import heapq

sys.stdin = open('input.txt', 'r')

# input = sys.stdin.readline


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
        if self.jump != other.jump:
            return self.jump < other.jump
        if self.r + self.c != other.r + other.c:
            return self.r + self.c < other.r + other.c
        if self.r != other.r:
            return self.r < other.r
        if self.c != other.c:
            return self.c < other.c
        return self.pid < other.pid


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
    next_rabbit = Rabbit(0, 0, 0, 0)
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
    up_rabbit = Rabbit(tmp_r, rabbit.c, 0, 0)
    if compare(next_rabbit, up_rabbit):
        next_rabbit = up_rabbit
    # 하
    tmp_r = rabbit.r + d_r
    if tmp_r > N:
        tmp_d = tmp_r - N
        tmp_r = N - tmp_d
        if tmp_r < 1:
            tmp_d = 1 - tmp_r
            tmp_r = 1 + tmp_d
    loc.append((tmp_r, rabbit.c))
    down_rabbit = Rabbit(tmp_r, rabbit.c, 0, 0)
    if compare(next_rabbit, down_rabbit):
        next_rabbit = down_rabbit
    # 좌
    tmp_c = rabbit.c - d_c
    if tmp_c < 1:
        tmp_d = 1 - tmp_c
        tmp_c = 1 + tmp_d
        if tmp_c > M:
            tmp_d = tmp_c - M
            tmp_c = M - tmp_d
    loc.append((rabbit.r, tmp_c))
    left_rabbit = Rabbit(rabbit.r, tmp_c, 0, 0)
    if compare(next_rabbit, left_rabbit):
        next_rabbit = left_rabbit
    # 우
    tmp_c = rabbit.c + d_c
    if tmp_c > M:
        tmp_d = tmp_c - M
        tmp_c = M - tmp_d
        if tmp_c < 1:
            tmp_d = 1 - tmp_c
            tmp_c = 1 + tmp_d
    loc.append((rabbit.r, tmp_c))
    right_rabbit = Rabbit(rabbit.r, tmp_c, 0, 0)
    if compare(next_rabbit, right_rabbit):
        next_rabbit = right_rabbit
    # print(loc)


    # loc.sort(key=cmp_to_key(comparator_loc))
    # print(loc)
    return next_rabbit.r, next_rabbit.c

# 가장 긴 위치를 판단하기 위해 정렬함수를 하나 더 만들어줍니다.
def compare(a, b):
    if a.r + a.c != b.r + b.c:
        return a.r + a.c < b.r + b.c
    if a.r != b.r:
        return a.r < b.r
    if a.c != b.c:
        return a.c < b.c
    return a.pid < b.pid


# 입력 받기
is_runned = {}
total_sum = 0
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

        for rabbit in rabbits.values():
            is_runned[rabbit.pid] = 0

        rabbit_pq = []

        for rabbit in rabbits.values():
            heapq.heappush(rabbit_pq, rabbit)

        for _ in range(K):
            # print_rabbit(rabbits)
            # 토끼 선정
            cur_rabbit = heapq.heappop(rabbit_pq)
            # print(cur_rabbit)
            # 움직인 토끼 pid 저장
            move_pid = cur_rabbit.pid
            # print(move_pid)
            is_runned[move_pid] = 1

            # print(move_pid)
            # 이동 선택
            nr, nc = select_move(cur_rabbit, N, M)
            # 이동
            rabbits[move_pid].r = nr
            rabbits[move_pid].c = nc
            rabbits[move_pid].jump += 1

            heapq.heappush(rabbit_pq, rabbits[move_pid])

            # 점수 산정
            rabbits[move_pid].score -= (nr + nc)
            total_sum += (nr + nc)
            # for key in rabbits.keys():
            #     if key != move_pid:
            #         rabbits[key].score += (nr + nc)
        # K턴 이후 최고 토끼 +S
        tmp_rabbits = []
        # print(set_move_pid)
        bonus_rabbit = Rabbit(0, 0, 0, 0)
        while rabbit_pq:
            cur_rabbit = heapq.heappop(rabbit_pq)

            if is_runned[cur_rabbit.pid] == 0:
                continue

            if compare(bonus_rabbit, cur_rabbit):
                bonus_rabbit = cur_rabbit
        rabbits[bonus_rabbit.pid].score += S
    elif cmd[0] == 300:  # 이동거리 변경
        pid = cmd[1]
        L = cmd[2]
        rabbits[pid].d *= L
    elif cmd[0] == 400:  # 최고 토끼 선정
        result = 0
        for rabbit in rabbits.values():
            if result < rabbit.score + total_sum:
                result = rabbit.score + total_sum
        print(result)
