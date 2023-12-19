import sys
from queue import PriorityQueue

sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

p_que = PriorityQueue()

for num in nums:
    p_que.put(num)

for i in range(m):
    x = p_que.get()
    y = p_que.get()
    p_que.put(x + y)
    p_que.put(x + y)

result = 0
while not p_que.empty():
    result += p_que.get()

print(result)

