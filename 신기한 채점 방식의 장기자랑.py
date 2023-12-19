def GetMaxScore(scores):
    dp = 0
    i = 0
    while i < len(scores):
        if scores[i] >= 0:
            dp += scores[i]
            i += 1
        else:
            flag = False
            case = [0, 0]
            while i < len(scores):
                if scores[i] >= 0:
                    dp += scores[i] + max(case)
                    i += 1
                    flag = True
                    break
                else:
                    case[i % 2] += scores[i]
                    i += 1
            if flag == False:
                dp += max(case)
    return dp

print(GetMaxScore([-5, -6, -7, -8, -9, 10]))
print(GetMaxScore([-3,2,4,-1,-2,-5])) # 4
print(GetMaxScore([5,-1,2,-3,4,-1])) # 11
print(GetMaxScore([-10,-7,-8,-4,6,-2,9])) # 4