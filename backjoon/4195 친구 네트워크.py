import sys

sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

def find_parent(parent_dict, x):
    if parent_dict[x] != x:
        parent_dict[x] = find_parent(parent_dict, parent_dict[x])
    return parent_dict[x]

def union_parent(parent_dict, parent_cnt, a, b):
    a = find_parent(parent_dict, a)
    b = find_parent(parent_dict, b)
    # print(a, b)
    if a != b:
        parent_dict[b] = a
        parent_cnt[a] += parent_cnt[b]
    print(parent_cnt[a])



T = int(input())
for _ in range(T):
    parent_dict = {}
    parent_cnt = {}
    F = int(input())
    for _ in range(F):
        a, b = input().split()
        if parent_dict.get(a, -1) == -1:
            parent_dict[a] = a
            parent_cnt[a] = 1
        if parent_dict.get(b, -1) == -1:
            parent_dict[b] = b
            parent_cnt[b] = 1
        union_parent(parent_dict, parent_cnt, a, b)