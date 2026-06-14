words = input("Enter sentence")

mylist = words.split()
new_list = mylist[::-1]

print(f"Original : {' '.join(mylist)}")
print(f"Reversed : {' '.join(new_list)}")
