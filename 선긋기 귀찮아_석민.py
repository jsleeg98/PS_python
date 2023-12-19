def getMergedLineSegments(Lines):
    Lines.sort()
    print("Lines : ",Lines)
    result=[]

    for idx in range(len(Lines)):
        s,l=Lines[idx]
        if idx==0:
            start,last=s,l
            continue

        if s<=last:
            last=max(l,last)
        else:
            result.append([start,last])
            start,last=s,l

    if len(result)==0:
        result.append([start,last])
    elif result[-1] != [start,last]:
      result.append([start,last])
    print(result)


getMergedLineSegments([[6,9],[2,3],[9,11],[1,5],[14,18]])
# [[1,5],[6,9],[14,18]]
getMergedLineSegments([[4,8],[2,6],[5,7]])
# [[2,8]]