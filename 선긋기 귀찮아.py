def getMergedLineSegments(li):
    li.sort(key=lambda x: (x[0], -x[1]))

    results = [li[0]]
    for l in li[1:]:
        s, e = l[0], l[1]
        flag = False
        for result in  results:
            ss, ee = result[0], result[1]
            if ss <= s <= ee and ss <= e <= ee:
                flag = True
                break
            elif ss <= s <= ee and ee <= e:
                result[1] = e
                flag = True
                break
        if not flag:
            results.append(l)

    return results


print(getMergedLineSegments([[6, 9], [2, 3], [9, 11], [1, 5], [14, 18]]))
print(getMergedLineSegments([[4, 8], [2, 6], [5, 7]]))



