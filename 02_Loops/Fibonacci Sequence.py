choice = int(input("How many Fibonacci numbers: "))

a,b = 0,1
mylist = []
for i in range(1,choice+1):
    mylist.append(a)
    a,b = b, a+b

print("Fibonacci sequence", *mylist)

check_a_number = int(input("Check a numbr: "))
if check_a_number in mylist:
    print(f"{check_a_number} is a Fibonacci number!")
else:
    print(f"{check_a_number} is not a Fibonacci number!")
