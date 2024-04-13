import sys

sys.stdin = open('input.txt', 'r')



max_score = 0
score = 0
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
block_dir = [0,
             [2, 3, 1, 0],
             [1, 3, 0, 2],
             [3, 2, 0, 1],
             [2, 0, 3, 1],
             [2, 3, 0, 1]
             ]
board = []
N = 0
warm = [] * 11
tmp_board = []

def init():
    global max_score, score, board, N, warm

    board = []
    N = int(input())
    for _ in range(N):
        board.append(list(map(int, input().split())))
    max_score = 0
    score = 0
    warm = [[] for _ in range(11)]

    # 웜홀 위치 초기화
    for r in range(N):
        for c in range(N):
            if 6 <= board[r][c] <= 10:
                warm[board[r][c]].append((r, c))

    print(warm)
def inRange(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    else:
        return False

def dfs(r, c, d, sr, sc, flag):
    global max_score, score
    if flag == True:  # 맨 처음이 아닌 경우
        if r == sr and c == sc:  # 시작 위치로 돌아온 경우 종료
            if max_score < score:
                max_score = score
            return
        if inRange(r, c):
            if board[r][c] == -1:  # 블랙홀인 경우 종료
                if max_score < score:
                    max_score = score
                return
    # print(r, c, score)
    # if inRange(r, c):
    #     tmp_board[r][c] = -2
    # for tmp_r in range(N):
    #     for tmp_c in range(N):
    #         print(tmp_board[tmp_r][tmp_c] , end=' ')
    #     print()
    # print()

    # 현위치 블록 파악
    # 바깥인 경우 - 방향 바꾸고 다음 이동
    if not inRange(r, c):
        score += 1  # 점수 추가
        d = (d + 2) % 4  # 방향 반대로 전환
        nr = r + dir[d][0]
        nc = c + dir[d][1]
    # 빈칸인 경우 그냥 이동
    elif board[r][c] == 0:
        nr = r + dir[d][0]
        nc = c + dir[d][1]
    # 블록인 경우 - 방향 바꾸고 다음 이동
    elif board[r][c] == 1:  # 1번 블록이 부딫힌 경우
        score += 1  # 점수 추가
        d = block_dir[1][d]  # 방향 전환
        # 다음위치
        nr = r + dir[d][0]
        nc = c + dir[d][1]
    elif board[r][c] == 2:  # 2번 블록이 부딫힌 경우
        score += 1  # 점수 추가
        d = block_dir[2][d]  # 방향 전환
        # 다음위치 다시 계산
        nr = r + dir[d][0]
        nc = c + dir[d][1]
    elif board[r][c] == 3:  # 3번 블록이 부딫힌 경우
        score += 1  # 점수 추가
        d = block_dir[3][d]  # 방향 전환
        # 다음위치 다시 계산
        nr = r + dir[d][0]
        nc = c + dir[d][1]
    elif board[r][c] == 4:  # 4번 블록이 부딫힌 경우
        score += 1  # 점수 추가
        d = block_dir[4][d]  # 방향 전환
        # 다음위치 다시 계산
        nr = r + dir[d][0]
        nc = c + dir[d][1]
    elif board[r][c] == 5:  # 5번 블록이 부딫힌 경우
        score += 1  # 점수 추가
        d = block_dir[5][d]  # 방향 전환
        # 다음위치 다시 계산
        nr = r + dir[d][0]
        nc = c + dir[d][1]
    elif 6 <= board[r][c] <= 10:  # 웜홀에 빠진 경우
        tmp_warm = warm[board[r][c]]
        if tmp_warm[0][0] == r and tmp_warm[0][1] == c:
            nr = tmp_warm[1][0]
            nc = tmp_warm[1][1]
        else:
            nr = tmp_warm[0][0]
            nc = tmp_warm[0][1]
        nr = nr + dir[d][0]
        nc = nc + dir[d][1]
    # dfs(nr, nc, d, sr, sc, True)

T = int(input())
for test_case in range(1, T + 1):
    init()
    for r in range(N):
        for c in range(N):
            # 빈칸인 경우
            if board[r][c] == 0:
                for d in range(4):
                    score = 0
                    dfs(r, c, d, r, c, False)
    print(f'#{test_case} {max_score}')
