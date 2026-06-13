a= int(input("Enter the size of the list"))
inputlist = []
for _ in range(1,a+1):
    n = int(input())
    inputlist.append(n)

for j in range (a):
    if inputlist[j] == inputlist[a-j-1]:
        inputlist.pop[inputlist[a-j]]
        inputlist.append(inputlist[j])
    else :
        pass

print(inputlist)
