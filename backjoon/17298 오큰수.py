import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
li = list(map(int, input().split()))

li.reverse()

stack = []
result = []

for i in li:
    if not stack:
        result.append(-1)
    else:
        if stack[-1] > i:
            result.append(stack[-1])
        else:
            while stack:
                if stack[-1] <= i:
                    stack.pop()
                else:
                    break

            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1])
    stack.append(i)

# result.reverse()

while result:
    print(result.pop(), end=' ')

# for i in result:
#     print(i, end=' ')