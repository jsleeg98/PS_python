cnt = 0

def backtracking(depth, cur_arr, t, start, d):
    global cnt
    if depth == 3:
        if sum(cur_arr) <= t:
            cnt += 1
        return

    for i in range(start, len(d) - 2 + depth):
        cur_arr.append(d[i])
        backtracking(depth+1, cur_arr, t, start, d)
        cur_arr.pop()
def three_numbers(t, d):
    global cnt
    d = sorted(d)

    cnt = 0
    depth = 0
    cur_arr = []
    backtracking(depth, cur_arr, t, 0, d)
    return cnt




print(three_numbers(1, [3, 1, 2]))