num = int(input("Enter the Number:"))
steps = 0
mylist = [int(d) for d in str(num)]
while len(mylist) > 1:
    total = sum(mylist)
    mylist = [int(d) for d in str(total)]
    steps += 1
        
if steps == 0:
    print(f"The number {num} is already single digit")
else :
    print("Digital Root: ", mylist[0])
    print("Steps:", steps)
