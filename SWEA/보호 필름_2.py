import sys
sys.stdin = open('input.txt', 'r')

D = 0  # 두께
W = 0  # 너비
K = 0  # 기준
board = []  # 막 정보
flag = False  # 가능 여부
min_cnt = 14  # 최소 횟수

def init():
    global D, W, K, board, min_cnt

    D, W, K = map(int, input().split())

    board = [[]]

    for i in range(D):
        tmp = list(map(int, input().split()))
        board.append([-1] + tmp)

    min_cnt = 14

def check():
    flag_in = True  # 가능 여부
    # 각 열마다 체크
    for c in range(1, W + 1):
        max_len = 0
        tmp = [board[1][c]]
        for r in range(2, D + 1):
            if board[r][c] == tmp[-1]:
                tmp.append(board[r][c])
            else:
                tmp_len = len(tmp)
                if max_len < tmp_len:
                    max_len = tmp_len
                tmp = [board[r][c]]
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

def print_board(board):
    for r in range(1, D + 1):
        for c in range(1, W + 1):
            print(f'{board[r][c]:<3}', end=' ')
        print()
    print('-' * 20)

def dfs(cnt, cur_d):
    global min_cnt, board
    if check() == True or cnt == K:
        if min_cnt > cnt:
            min_cnt = cnt
        return

    for i in range(cur_d, D + 1):
        # 원래 값 저장
        ori_d = [0] * (W + 1)
        for c in range(1, W + 1):
            ori_d[c] = board[i][c]
        # 0으로 바꾸기
        for c in range(1, W + 1):
            board[i][c] = 0
        dfs(cnt + 1, i + 1)  # 다음 확인

        # 1로 바꾸기
        for c in range(1, W + 1):
            board[i][c] = 1
        dfs(cnt + 1, i + 1)  # 다음 확인

        # 원래대로 바꾸기
        for c in range(1, W + 1):
            board[i][c] = ori_d[c]

T = int(input())
for test_case in range(1, T + 1):
    init()
    # print_board(board)
    if not K == 1:
        dfs(0, 1)
        print(f'#{test_case} {min_cnt}')
    else:
        print(f'#{test_case} {0}')