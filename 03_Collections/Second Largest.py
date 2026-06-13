mylist = [int(x) for x in input("Enter numbers (space separated): ").split()]

max1 = max2 = float('-inf')

for num in mylist:
    if num > max1:
        max2 = max1    # old largest becomes second
        max1 = num     # new largest
    elif num > max2 and num != max1:
        max2 = num

if max2 == float('-inf'):
    print("No second largest exists!")
else:
    print(f"Second largest: {max2}")
