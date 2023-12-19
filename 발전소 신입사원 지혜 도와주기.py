# import collections
#
# def GetMaxTime(energy, th):
#     dic = collections.defaultdict(int)
#     max_e = max(energy)
#     for e in energy:
#         e = max_e - e
#         if e not in dic:
#             dic[e] = 1
#         else:
#             dic[e] += 1
#
#     cur = 0
#     up = 0
#     cnt = 0
#     for i in range(max_e):
#         up += dic[i]
#         cur += up
#         cnt += 1
#         if cur >= th:
#             break
#
#     print(cnt)
#     return max_e - cnt
#
#
# print(GetMaxTime([100000000], 99999999))

def GetMaxTime(initialEnergy=[], th=0):
    initialEnergy.sort()
    start = 0
    end = initialEnergy[-1]

    while start <= end:
        copy_initialEnergy = initialEnergy.copy()
        mid = (start + end) // 2
        total_sum = 0
        copy_initialEnergy.reverse()
        for energy in copy_initialEnergy:
            if energy <= mid:
                break
            else:
                total_sum += energy - mid
        print(f'total_sum : {total_sum}')
        if total_sum > th:
            start = mid + 1
        else:
            end = mid - 1

    return mid

# print(GetMaxTime(initialEnergy=[4, 8, 7, 1, 2], th=9))
print(GetMaxTime([100000000], 1))

