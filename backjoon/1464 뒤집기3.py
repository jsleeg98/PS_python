import sys
import queue
from collections import deque

sys.stdin = open('input.txt', 'r')

de_1 = deque()
de_2 = deque()

str = input()

for i in str:
    de_1.append(i)

flag = False
if len(str) == 1:
    print(str)
    flag = True



if flag == False:
    while True:
        standard = de_1.popleft()
        de_2.append(standard)
        if standard < de_1[0]:
            while standard <= de_1[0]:
                tmp = de_1.popleft()
                de_2.append(tmp)
                standard = tmp
                if len(de_2) == len(str):
                    break
            while de_2:
                de_1.appendleft(de_2.popleft())
        elif standard > de_1[0]:
            while standard >= de_1[0]:
                tmp = de_1.popleft()
                de_2.append(tmp)
                standard = tmp
                if len(de_2) == len(str):
                    break
            while de_2:
                de_1.appendleft(de_2.popleft())
            break

    while de_1:
        print(de_1.popleft(), end='')






