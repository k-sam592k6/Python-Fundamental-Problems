n = int(input("Enter the size of the list: "))

mylist = []

for _ in range (1,n+1):
    a = int(input())
    mylist.append(a)

print(mylist)

for i in set(mylist):
    if mylist.count(mylist[i]) > n/2:
        print(i)
        break
    else:
        print("No majority element")
        pass
