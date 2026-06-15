def count_occurance(lst, target):
    count = 0

    for item in lst:
        if isinstance(item, list):
            count += count_occurance(item, target)

        elif item == target:
            count += 1

    return count


mylist1 = [1, [2, [1, 3], 1], 4]

target = int(input("Enter target: "))

print(count_occurance(mylist1, target))
