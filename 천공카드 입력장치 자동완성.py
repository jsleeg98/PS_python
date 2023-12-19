# inputs = ['100110', '1001', '1001111']
inputs = ['000', '1110', '01', '001' '110', '11']



def print_log(li):
    for i, tmp in enumerate(li):
        print(f'{i} : {tmp}')
    print('-' * 20)
def autocompletes(inputs):
    li = []
    for i in range(31):
        li.append([[], []])

    results = []
    for i, input in enumerate(inputs):
        # print_log(li)
        result = []
        for idx in range(1, len(input) + 1, 1):
            if len(li[idx][int(input[idx-1])]) != 0:
                result = list(set(result) & set(li[idx][int(input[idx-1])]))
            li[idx][int(input[idx-1])].append(idx)

        if i == 0:
            results.append(0)
        elif result == -1:
            results.append(i)
        else:
            results.append(result)

    return results

results = autocompletes(inputs)
print(results)