from collections import defaultdict

word = input()

di = defaultdict(lambda: 0)


for w in word:
    tmp = w.lower()
    if di[tmp] != 0:
        di[tmp] += 1
    else:
        di[tmp] = 1

li = []
for key in di.keys():
    li.append((di[key], key))

li.sort()
if len(li) > 1:
    if li[-1][0] == li[-2][0]:
        print('?')
    else:
        print(li[-1][1].upper())
else:
    print(li[-1][1].upper())