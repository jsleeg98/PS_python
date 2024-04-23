H, W, N, M = map(int, input().split())

a = H // (N + 1)
b = W // (M + 1)

if H % (N + 1) > 0:
    a += 1
if W % (M + 1) > 0:
    b += 1

print(a * b)