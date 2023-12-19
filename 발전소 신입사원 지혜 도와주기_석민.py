def GetMaxTime(initialEnergy=[], th=0):
    Energy_len = len(initialEnergy)
    initialEnergy.sort()
    copy_initialEnergy = initialEnergy.copy()

    Start = 0
    End = initialEnergy[-1]

    if sum(initialEnergy) <= th:
        print(0)
        return 0

    while Start <= End:
        total_sum = 0
        mid = (Start + End) // 2
        copy_initialEnergy = initialEnergy.copy()
        for idx in range(Energy_len - 1, -1, -1):
            copy_initialEnergy[idx] -= mid
            s = max(0, copy_initialEnergy[idx])
            total_sum += s
            if s == 0:
                break
        print("total_sum : ", total_sum)
        if total_sum > th:
            Start = mid + 1
        else:
            End = mid - 1

    print(mid)


# GetMaxTime(initialEnergy=[4, 8, 7, 1, 2], th=9)
GetMaxTime(initialEnergy=[100000000], th=1)