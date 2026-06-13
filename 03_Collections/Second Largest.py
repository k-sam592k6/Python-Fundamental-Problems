mylist =  [int(x) for x in input("Enter numbers (space separated):").split()]

max1 = max2 = float('-inf')

for num in mylist:
    if num > max1:
        max1 = max2 
        max1 = num
    elif num >  max2 and num != max1:
        max2 = num

print(max2)
