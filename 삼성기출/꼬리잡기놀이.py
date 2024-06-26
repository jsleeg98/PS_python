import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
import queue

train_length = []
board = []  # 0행 0열 시작
trains = []  # 0번 기차부터 시작
dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
nxt = [(1, 0), (0, 1), (-1, 0), (0, -1)]
tmp_cnt = 0
nxt_idx = -1
visit = []
train_board = []
sr = 0
sc = 0
total_score = 0
is_left = []

n, m, k = map(int, input().split())

is_left = [True for _ in range(n)]

for i in range(n):
    board.append(list(map(int, input().split())))

for i in range(m):
    trains.append(deque())

def inRange(r, c):
    if 0 <= r <= n-1 and 0 <= c <= n-1:
        return True
    else:
        return False

def dfs(train_idx, cr, cc, length):
    global visit
    trains[train_idx].append((cr, cc))
    can_component = 5
    can_r = 0
    can_c = 0
    for i in range(4):
        nr = cr + dir[i][0]
        nc = cc + dir[i][1]
        if not inRange(nr, nc):
            continue
        if visit[nr][nc] == 1:
            continue
        if board[nr][nc] == 2:
            length += 1
            if can_component > 2:
                can_component = 2
                can_r = nr
                can_c = nc
        elif board[nr][nc] == 3:
            if can_component > 3:
                can_component = 3
                can_r = nr
                can_c = nc
        elif board[nr][nc] == 4:
            if can_component > 4:
                can_component = 4
                can_r = nr
                can_c = nc
    if can_component != 5:
        visit[can_r][can_c] = 1
        dfs(train_idx, can_r, can_c, length)
    else:
        train_length.append(length + 1)

def update_line():
    global tmp_cnt, nxt_idx, sr, sc
    if tmp_cnt == 0:
        tmp_cnt += 1
        nxt_idx += 1
        nxt_idx = nxt_idx % 4
    else:
        tmp_cnt += 1
        tmp_cnt = tmp_cnt % n
        sr = sr + nxt[nxt_idx][0]
        sc = sc + nxt[nxt_idx][1]

# 기차 정보 획득
train_idx = 0
for r in range(n):
    for c in range(n):
        if board[r][c] == 1:
            visit = [[0 for _ in range(n)] for _ in range(n)]
            visit[r][c] = 1
            dfs(train_idx, r, c, 1)
            train_idx += 1

for _ in range(k):
    # 기차 전진
    for i in range(m):
        if is_left[i]:
            tmp = trains[i].pop()
            trains[i].appendleft(tmp)
        # else:


    # 보드에 기차 번호 표시
    train_board = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        for l in range(train_length[i]):
            # print(trains[i][l], end=' ')
            r, c = trains[i][l]
            train_board[r][c] = i
    # print()
    # for r in range(n):
    #     for c in range(n):
    #         print(f'{train_board[r][c]:<3}', end=' ')
    #     print()
    # print('-' * 20)
    # print(trains)

    # 공 던지기
    attacked_train = {}
    update_line()  # 공 시작 위치 sr, sc
    for i in range(n):
        nr = sr + dir[nxt_idx][0] * i
        nc = sc + dir[nxt_idx][1] * i
        # print(f'({nr}, {nc})', end=' ')
        if train_board[nr][nc] != -1:  # 기차가 있는 위치인 경우
            if not train_board[nr][nc] in attacked_train.keys():  # 처음 만난 겨우
                attacked_train[train_board[nr][nc]] = (nr, nc)  # 기차 번호 : 위치
                break
    # print(attacked_train)

    # 점수 처리
    for key, value in attacked_train.items():
        # 기차 위치 찾기
        for i in range(len(trains[key])):
            if trains[key][i] == value:
                total_score += (i + 1) ** 2
                print(_, (i + 1) ** 2)
                break

    # 맞은 팀 방향 바꾸기
    for key in attacked_train.keys():
        # if key == 2:
            # print(key)
        for i in range(train_length[key]):
            tmp = trains[key].popleft()
            trains[key].append(tmp)
        trains[key].reverse()

print(total_score)
