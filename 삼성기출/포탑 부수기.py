import copy
import sys
from functools import cmp_to_key
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

class top:
    def __init__(self, a, t, rc, c, r):
        self.a = a
        self.t = t
        self.rc = rc
        self.c = c
        self.r = r

def print_sort(list_m):
    print('-' * 20)
    for m in list_m:
        print(m.a, m.t, m.rc, m.r, m.c)
    print('-' * 20)

def comparator(a, b):
    if a.a < b.a:
        return -1
    elif a.a == b.a:
        if a.t > b.t:
            return -1
        elif a.t == b.t:
            if a.rc > b.rc:
                return -1
            elif a.rc == b.rc:
                if a.c > b.c:
                    return -1
                else:
                    return 1
            else:
                return 1
        else:
            return 1
    else:
        return 1


def find_top(tmp):
    tmp.sort(key=cmp_to_key(comparator))
    # print_sort(tmp)
    return tmp[0], tmp[-1]


dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상

# def dfs(r, c, path, er, ec, m, visit):
#     global final_path, flag
#     print(r, c)
#     if r == er and c == ec:
#         if flag == False:
#             final_path = path
#             flag = True
#         else:
#             if len(final_path) > len(path):
#                 final_path = path
#         return
#     else:
#         visit[r][c] = 1
#         for i in range(4):
#             nr = r + dir[i][0]
#             nc = c + dir[i][1]
#             if nr == 0:
#                 nr = 4
#             if nc == 0:
#                 nc = 4
#             if nr == 5:
#                 nr = 1
#             if nc == 5:
#                 nc = 1
#             if m[nr][nc].a != 0 and visit[nr][nc] == 0:
#                 path.append((r, c))
#                 dfs(nr, nc, path, er, ec, m, visit)


def bfs(r, c, er, ec, m):
    visit = [[0 for c in range(M + 1)] for r in range(N + 1)]
    path = [[[] for c in range(M + 1)] for r in range(N + 1)]
    q = deque()
    q.append((r, c))
    visit[r][c] = 1
    path[r][c].append((r, c))
    final_path = []
    flag = False
    while q:
        cr, cc = q.popleft()
        tmp_path = path[cr][cc]
        # print(cr, cc)
        # print(path)
        if flag:
            break

        # print(cr, cc)
        # print(tmp_path)
        for i in range(4):
            nr = cr + dir[i][0]
            nc = cc + dir[i][1]
            if nr == 0:
                nr = N
            if nc == 0:
                nc = M
            if nr == N + 1:
                nr = 1
            if nc == M + 1:
                nc = 1
            if m[nr][nc].a != 0 and visit[nr][nc] == 0:
                if nr == er and nc == ec:
                    flag = True
                    final_path = tmp_path
                    break
                q.append((nr, nc))
                visit[nr][nc] = 1
                new_path = tmp_path + [(nr, nc)]
                path[nr][nc] = new_path

    return final_path

def laser(m, sr, sc, er, ec):
    final_path = bfs(sr, sc, er, ec, m)
    return final_path

def attack_top(m, attack, defence, path, k):
    m[attack.r][attack.c].a += (N + M)
    m[attack.r][attack.c].t = k
    damage = m[attack.r][attack.c].a
    m[defence.r][defence.c].a -= damage
    for p in path:
        m[p[0]][p[1]].a -= (damage // 2)

boom_dir = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
def boom(m, sr, sc, er, ec):
    path = []
    for i in range(8):
        nr = er + boom_dir[i][0]
        nc = ec + boom_dir[i][1]
        if nr == 0:
            nr = N
        if nc == 0:
            nc = M
        if nr == N + 1:
            nr = 1
        if nc == M + 1:
            nc = 1
        if m[nr][nc].a != 0:
            if nr != sr or nc != sc:
                path.append((nr, nc))

    return path

def break_top(m):
    non_zero_m = []
    for r in range(1, N+1):
        for c in range(1, M+1):
            if m[r][c].a <= 0:
                m[r][c].a = 0
            else:
                non_zero_m.append(m[r][c])
    return non_zero_m


def up(m, final_path):
    max_a = 0
    mm = copy.deepcopy(m)
    for f in final_path:
        mm[f[0]][f[1]].a = 0

    for r in range(1, N+1):
        for c in range(1, M+1):
            if mm[r][c].a != 0:  # 공격에 연관되지 않고 공격력이 0이 아닌 경우
                m[r][c].a += 1
            if max_a < m[r][c].a:
                max_a = m[r][c].a
    return max_a
def print_top(m):
    print('-' * 30)
    for r in range(1, N+1):
        for c in range(1, M+1):
            print(m[r][c].a, end=' ')
        print()
    print('-' * 30)

def check_top(m):
    cnt = 0
    max_attack = 0
    for r in range(1, N+1):
        for c in range(1, M+1):
            if m[r][c].a > 0:
                cnt += 1
                if max_attack < m[r][c].a:
                    max_attack = m[r][c].a
    if cnt == 1:
        return True, max_attack
    elif cnt == 0:
        return True, max_attack
    else:
        return False, max_attack

N, M, K = map(int, input().split())
m = [[0 for i in range(M + 1)] for j in range(N + 1)]

non_zero_m = []

for r in range(1, N + 1):
    tmp = list(map(int, input().split()))
    for c in range(1, M + 1):
        a = tmp[c - 1]
        t = 0
        rc = r + c
        c = c
        tmp_top = top(a, t, rc, c, r)
        m[r][c] = tmp_top
        if a > 0:
            non_zero_m.append(m[r][c])

for k in range(1, K+1):
    final_path = []
    # 공격자 후보 찾기
    min_attack = 5001
    attack_can = []
    for i in non_zero_m:
        if i.a < min_attack:
            min_attack = i.a
            attack_can = [i]
        elif i.a == min_attack:
            attack_can.append(i)
    attack, _ = find_top(attack_can)
    # 방어자 후보 찾기
    max_attack = 0
    defense_can = []
    for i in non_zero_m:
        if i.a > max_attack:
            max_attack = i.a
            defense_can = [i]
        elif i.a == max_attack:
            defense_can.append(i)
    _, defense = find_top(defense_can)
    # 공격자 찾기, 방어자 찾기
    # attack, defense = find_top(non_zero_m)
    # print(attack.r, attack.c)
    # print(defense.r, defense.c)
    # print('-' * 20)
    # 레이저 공격 or 포탑 공격
    final_path = laser(m, attack.r, attack.c, defense.r, defense.c)
    # print(final_path)
    if len(final_path) > 0:
        final_path = final_path[1:]
        attack_top(m, attack, defense, final_path, k)
    else:
        final_path = boom(m, attack.r, attack.c, defense.r, defense.c)
        attack_top(m, attack, defense, final_path, k)
    final_path.append((attack.r, attack.c))
    final_path.append((defense.r, defense.c))
    non_zero_m = break_top(m)
    # 정비
    max_a = up(m, final_path)
    # print_top(m)
    # check, max_attack = check_top(m)
    # if check:
    #     break
    if len(non_zero_m) <= 1:
        break


print(max_a)