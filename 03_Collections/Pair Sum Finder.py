n=int(input("Size of the list: "))
mylist = []
for _ in range(1,n+1):
    a = int(input())
    mylist.append(a)

target = int(input("Enter target:"))

mylistfinal= []
for i in range(len(mylist)):
    for j in range(i+1, len(mylist)):
        if mylist[i]  + mylist[j] == target:
            mylistfinal.append(mylist(i), mylist(j))

if len(mylistfinal) == 0:
    print("No pairs found!")
else:
    print(f"\nPairs that sum to {target}:")
    for pair in mylistfinal:
        print(pair)
    print(f"\n Total pairs found: {len(memoryview)}")
