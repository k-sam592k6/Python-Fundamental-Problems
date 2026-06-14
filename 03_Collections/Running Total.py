data = input("Enter numbers (space separated): ")

mylist = [int(x) for x in data]
n = len(mylist)

total = 0
final_list = []
for num in mylist:
    total = total + num
    final_list.append(total)
    

print("Orignal: ", mylist)
print("Running Total: ", final_list)
