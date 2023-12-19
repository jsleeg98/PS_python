import sys
from queue import PriorityQueue

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
p_que = PriorityQueue()

for i in range(N):
    inp = abs(int(sys.stdin.readline()))
    if inp == 0:
        if p_que.empty():
            print(0)
        else:
            tmp = p_que.get()
            print(tmp)
            while True and not p_que.empty():
                tmp_2 = p_que.get()
                if tmp == tmp_2:
                    pass
                else:
                    p_que.put(tmp_2)
                    break
    else:
        p_que.put(inp)
