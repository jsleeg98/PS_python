import sys

sys.stdin = open('input.txt', 'r')

def inRange(r, c):
    if 0 <= r < H and 0 <= c < W:
        return True
    else:
        return False

dir = [(-1, 0), (0, 1), (0, -1), (1, 0)]
def dfs(N, total, board):
    global broken_blocks
    if N == 0:
        if broken_blocks < total:
            broken_blocks = total
        return
    elif total_blocks == total:
        broken_blocks = total
        return

    for c in range(W):
        arr = [x[:] for x in board]
        stack = set()
        blocks = 0

        # 맨 위에 있는 블럭 찾기
        for r in range(H):
            if arr[r][c] != 0:
                stack.add((r, c))
                break

        while stack:
            cr, cc = stack.pop()
            if arr[cr][cc] == 0:
                continue

            blocks += 1  # 부서진 블럭 추가

            P = arr[cr][cc]
            for p in range(1, P):
                for i in range(4):
                    nr = cr + dir[i][0] * p
                    nc = cc + dir[i][1] * p
                    if not inRange(nr, nc):  # 범위 밖
                        continue  # 해당 방향 종료
                    stack.add((nr, nc))  # 스택에 추가
            arr[cr][cc] = 0  # 해당 칸 비우기

        # 중력
        for c in range(W):
            idx = H - 1
            for r in range(H - 1, -1, -1):
                if arr[r][c] != 0:
                    arr[idx][c], arr[r][c] = arr[r][c], arr[idx][c]
                    idx -= 1

        dfs(N - 1, total + blocks, arr)

        # for r in range(H):
        #     for c in range(W):
        #         print(arr[r][c], end=' ')
        #     print()
        #
        # print('-' * 20)



T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = []
    for _ in range(H):
        board.append(list(map(int, input().split())))

    total_blocks = 0
    for r in range(H):
        for c in range(W):
            if board[r][c] != 0:
                total_blocks += 1

    broken_blocks = 0

    dfs(N, 0, board)

    print(f'#{test_case} {total_blocks - broken_blocks}')
