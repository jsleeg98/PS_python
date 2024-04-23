N = int(input())

cnt = 1
tmp = 1
adder = 6


while True:
    if tmp >= N:
        break
    tmp += adder
    adder += 6
    cnt += 1

print(cnt)