import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    li = list(map(int, input().split()))
    T = li[0]
    li = li[1:]
    sort_li = []
    sort_li.append(li[0])
    ans = 0
    for num in li[1:]:
        cnt = 0
        insert_idx = 0
        for i in range(len(sort_li)):
            idx = len(sort_li) - i - 1
            if sort_li[idx] > num:
                cnt += 1
                insert_idx = idx
        if cnt > 0:
            ans += len(sort_li) - insert_idx
            sort_li.insert(insert_idx, num)
        else:
            sort_li.append(num)
    print(T, ans)