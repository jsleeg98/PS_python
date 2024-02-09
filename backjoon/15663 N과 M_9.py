import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

nums = list(map(int, input().split()))

set_nums = sorted(list(set(nums)))

dic_nums = {}
for i in set_nums:
    dic_nums[i] = nums.count(i)

answers = [[] for i in range(M)]


def dfs(N, M, dic_nums, li_cur, answers, cur_pos):
    if len(li_cur) == M:
        for num in li_cur:
            print(num, end=' ')
        print()
    for key in dic_nums.keys():
        if dic_nums[key] > 0:
                if cur_pos < M:
                    if not key in answers[cur_pos]:
                        dic_nums[key] -= 1
                        answers[cur_pos].append(key)
                        li_cur.append(key)
                        dfs(N, M, dic_nums, li_cur, answers, cur_pos + 1)
                        dic_nums[key] += 1
                        answers[cur_pos].pop()
                        li_cur.pop()

dfs(N, M, dic_nums, li_cur=[], answers=answers, cur_pos=0)
