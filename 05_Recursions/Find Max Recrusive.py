def maxvalue(lst):

    if len(lst) == 1:
        return lst[0]

    if len(set(lst)) == 1:
        return lst[0]

    final_list = []

    for i in range(len(lst)):
        if lst[i] >= lst[i - 1]:
            final_list.append(lst[i])

    return maxvalue(final_list)


lst = [int(x) for x in input("Enter numbers: ").split()]

print(maxvalue(lst))
