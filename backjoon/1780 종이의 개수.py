import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

arr = []
for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
# print(arr)
def check(mat):
    print(mat)
    ch = mat[0][0]
    flag = True
    for r in range(len(mat)):
        for c in range(len(mat)):
            if ch != mat[r][c]:
                flag = False
                break
    return flag

answer = [0, 0, 0]
def dfs(mat):
    if len(mat) == 1:
        answer[mat[0][0] + 1] += 1
    elif check(mat):
        answer[mat[0][0]+1] += 1

    else:
        per = len(mat) // 3
        cnt_r = 0
        cnt_c = 0

        for i in range(9):
            tmp = []
            for r in range(cnt_r, cnt_r + per):
                tmptmp = []
                for c in range(cnt_c, cnt_c + per):
                    tmptmp.append(mat[r][c])
                tmp.append(tmptmp)
            dfs(tmp)

            if cnt_c == per * 2:
                cnt_c = 0
                cnt_r += per
            else:
                cnt_c += per

dfs(arr)

for ans in answer:
    print(ans)