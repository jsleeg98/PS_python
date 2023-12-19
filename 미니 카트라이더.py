# obstacleLanes = [2, 1, 3, 2]
# obstacleLanes = [2, 1, 2]
obstacleLanes = [2,1,1,2,1,2,1,2,1,2]   # 1
obstacleLanes = [2,1,3,2,1,3,2,1,3,2,2,3]   # 5
obstacleLanes = [1,3,2,1,3,2,1,3,2,2,3]   # 5


def minimumMovement(obstacleLanes):
    map = []
    for i in range(len(obstacleLanes)):
        map.append([1, 1, 1])
    for i, obstacle in enumerate(obstacleLanes):
        map[len(map)-i-1][obstacle-1] = -1
    # for m in map:
    #     print(m)
    # print('-' * 20)
    for i, m in enumerate(map[1:]):
        for j in range(3):
            if m[j] != -1 and map[i][j] != -1:
                map[i+1][j] += map[i][j]

    # for m in map:
    #     print(m)

    change = 0
    cur = 1
    for i in range(len(map)-1, -1, -1):
        if map[i][cur] == -1:
            left = (cur + 3 - 1) % 3
            right = (cur + 3 + 1) % 3
            if map[i-1][left] >= map[i-1][right]:
                cur = left
                change += 1
            else:
                cur = right
                change += 1
    return change


change = minimumMovement(obstacleLanes)
print(change)