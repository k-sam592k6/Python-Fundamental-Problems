n = int(input("Enter the size of the list:"))

list_required = []

for i in range (1,n+1):
    a = int(input())
    list_required.append(a)

a = len(list_required)
b = len(set(list_required))

if a > b :
    print("true") 
else:
    print("false")
