n = int(input("Size of the list: "))
mylist = []
for _ in range (n):
    num = int(input(f"Enter number {_+1}: "))
    mylist.append(num)

print("Numbers entred: ", mylist)
print(f"Mean: {(sum(mylist)) / len(mylist):.2f}")
print(f"Highest: {max(mylist)}")
print(f"Lowest: {min(mylist)}")
print(f"Range: {max(mylist) - min(mylist)}")
