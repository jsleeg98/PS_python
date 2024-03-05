import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

tree = {}
n = int(input())
for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == '.':
        left_node = None
    if right_node == '.':
        right_node = None
    tree[data] = Node(data, left_node, right_node)

def pre_order(Node):
    print(Node.data, end='')
    if Node.left_node != None:
        pre_order(tree[Node.left_node])
    if Node.right_node != None:
        pre_order(tree[Node.right_node])

def in_order(Node):
    if Node.left_node != None:
        in_order(tree[Node.left_node])
    print(Node.data, end='')
    if Node.right_node != None:
        in_order(tree[Node.right_node])

def post_order(Node):
    if Node.left_node != None:
        post_order(tree[Node.left_node])
    if Node.right_node != None:
        post_order(tree[Node.right_node])
    print(Node.data, end='')

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])