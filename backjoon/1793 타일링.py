import sys

sys.stdin = open('input.txt', 'r')

lines = sys.stdin.readlines()

mem = [-1 for i in range(251)]
mem[0] = 1  # 2x0 인 경우를 1로 취급
mem[1] = 1
mem[2] = 3

def tile(n):
    if n == 0 or n == 1:
        return mem[n]
    if n % 2 == 0:
        if mem[n-1] != -1:
            tmp = mem[n-1]
        else:
            tmp = tile(n-1)
        return 2 * tmp + 1
    else:
        if mem[n-1] != -1:
            tmp = mem[n-1]
        else:
            tmp = tile(n-1)
        return 2 * tmp - 1

for line in lines:
    print(tile(int(line.rstrip())))
