a = int(input("Enter the size of list 1: "))

list1 =[]
for _ in range (1, a+1):
    num1 = int(input("Enter list 1 : "))
    list1.append(num1)

b = int(input("Enter the size of list 2"))

list2 =[]
for _ in  range(1,b+1):
    num2 = int(input("Enter list 2 : "))
    list2.append(num2)

common_list  =[]
for item in list1:
    if item in list2 and item not in common_list:
        common_list.append(item)
    else:
        pass
if len(common_list) == 0:
    print("No common elements found")
else:
    print(common_list)

