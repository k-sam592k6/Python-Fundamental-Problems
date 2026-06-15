def nested_list(lst):

    total = 0

    for item in lst:
        if isinstance(item, list):
            total += nested_list(item)
        else:
            total += int(item)
        

    return total

lst = [1, [2, [3, [4, [5]]]]]
print(nested_list(lst))
