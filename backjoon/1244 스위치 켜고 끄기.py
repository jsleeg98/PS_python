import sys

sys.stdin = open('input.txt', 'r')

def change(a, b):
    if a == 1:
        for i in range(((len(switch) - 1) // b)):
            switch[b * (i + 1)] = (switch[b * (i + 1)] + 1) % 2
    elif a == 2:
        cnt = 1
        while True:
            L = b - cnt
            R = b + cnt
            if L < 1 or R > len(switch)-1:
                break
            if switch[L] == switch[R]:
                cnt += 1
            else:
                break
        for i in range(b - (cnt - 1), b + cnt):
            switch[i] = (switch[i] + 1) % 2

N = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
switch.insert(0, 3)

S = int(sys.stdin.readline())
for i in range(S):
    a, b = map(int, sys.stdin.readline().split())
    change(a, b)

for i in range(1, len(switch)):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
