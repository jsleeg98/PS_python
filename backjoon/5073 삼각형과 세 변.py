while True:
    li = list(map(int, input().split()))
    if li[0] == 0:
        break

    li.sort()
    if li[-1] >= li[0] + li[1]:
        print('Invalid')
    elif li[0] == li[1] and li[1] == li[2]:
        print('Equilateral')
    elif li[-1] == li[-2] or li[0] == li[1]:
        print('Isosceles')
    else:
        print('Scalene')
