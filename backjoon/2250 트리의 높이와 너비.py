import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

n = int(input())
tree = {}
for i in range(n):
    data, left, right = map(int, input().split())
    if left == -1:
        left = None
    if right == -1:
        right = None
    tree[data] = Node(data, left, right)

m = [() for i in range(n + 1)]
c = 1
max_depth = 0
def in_order(Node, depth):
    global c, max_depth
    if Node.left != None:
        in_order(tree[Node.left], depth + 1)
    m[Node.data] = (depth, c)
    c += 1
    if depth > max_depth:
        max_depth = depth
    if Node.right != None:
        in_order(tree[Node.right], depth + 1)

def find_root(tree):
    check = [0 for i in range(n + 1)]
    for key, value in tree.items():
        if value.left != None:
            check[value.left] = 1
        if value.right != None:
            check[value.right] = 1

    for i in range(1, n + 1):
        if check[i] == 0:
            return i


root = find_root(tree)
# print(root)
# print(tree)
in_order(tree[root], 1)

# for i in range(1, n + 1):
#     print(i, m[i][0], m[i][1])

width = [[] for i in range(max_depth + 1)]
for i in range(1, n + 1):
    width[m[i][0]].append(m[i][1])

result_depth = 0
result_width = 0
for i in range(1, max_depth + 1):
    mmin = min(width[i])
    mmax = max(width[i])
    wid = mmax - mmin + 1
    if result_width < wid:
        result_depth = i
        result_width = wid

print(result_depth, result_width)
