num = int(input("Enter a Number:"))

mylist = [num]
while num != 1:
    if num %2 == 0:
        num = num // 2
    else :
        num = (num * 3) + 1
    
    mylist.append(num)

print(*mylist, sep="-->")
print("Sequence Length:", len(mylist))
