import sys
sys.stdin = open('input.txt', 'r')

D = 0  # 두께
W = 0  # 너비
K = 0  # 기준
board = []  # 막 정보
flag = False  # 가능 여부

def init():
    global D, W, K, board

    D, W, K = map(int, input().split())

    board = [[]]

    for i in range(D):
        tmp = list(map(int, input().split()))
        board.append([-1] + tmp)

def change(li_AB, li_D):
    # li_AB에는 A로 바뀌는 것이 담겨 있고 나머지는 B
    li_A = li_AB
    li_B = []
    for i in range(len(li_D)):
        if not li_D[i] in li_A:
            li_B.append(li_D[i])

    # 염색할 보드 초기화
    tmp_board = [[0 for _ in range(W + 1)] for _ in range(D + 1)]

    for r in range(1, D + 1):
        for c in range(1, W + 1):
            tmp_board[r][c] = board[r][c]

    for a in li_A:
        for i in range(1, W + 1):
            tmp_board[a][i] = 0

    for b in li_B:
        for i in range(1, W + 1):
            tmp_board[b][i] = 1

    flag_in = True  # 가능 여부
    # 각 열마다 체크
    for c in range(1, W + 1):
        max_len = 0
        tmp = [tmp_board[1][c]]
        for r in range(2, D + 1):
            if tmp_board[r][c] == tmp[-1]:
                tmp.append(tmp_board[r][c])
            else:
                tmp_len = len(tmp)
                if max_len < tmp_len:
                    max_len = tmp_len
                tmp = [tmp_board[r][c]]
        # 마지막까지 같은 경우 처리
        tmp_len = len(tmp)
        if max_len < tmp_len:
            max_len = tmp_len

        if max_len < K:
            flag_in = False
            # print(c)
            break
    # if flag_in:
    #     print_board(tmp_board)

    return flag_in

def dfs_AB(li_AB, cur_idx, max_cnt, li_d):  # total : 총 개수
    global flag
    if len(li_AB) == max_cnt:
        flag = change(li_AB, li_d)
        return
    for i in range(cur_idx, len(li_d)):
        li_AB.append(li_d[i])
        dfs_AB(li_AB, i + 1, max_cnt, li_d)
        li_AB.pop()
        if flag == True:
            break

def check(li_d):
    global flag
    flag = False
    # 뽑힌 레이어 중 A, B 조합으로 가능한지 체크
    for i in range(0, len(li_d) + 1):
        dfs_AB([], 0, i, li_d)
        if flag == True:
            break



def dfs_layer(li_d, cur_idx, max_cnt):
    if len(li_d) == max_cnt:
        check(li_d)
        return
    for i in range(cur_idx, D + 1):
        li_d.append(i)
        dfs_layer(li_d, i + 1, max_cnt)
        li_d.pop()
        if flag == True:
            break

def print_board(board):
    for r in range(1, D + 1):
        for c in range(1, W + 1):
            print(f'{board[r][c]:<3}', end=' ')
        print()
    print('-' * 20)

T = int(input())
for test_case in range(1, T + 1):
    init()
    # print_board(board)
    min_k = 0
    if not K == 1:
        # 레이어 선택
        for i in range(0, K + 1):
            # print(i)
            dfs_layer([], 1, i)
            if flag == True:
                min_k = i
                break
    print(f'#{test_case} {min_k}')

