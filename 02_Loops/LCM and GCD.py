n1 = int(input("Enter number 1 :"))
n2 = int(input("Enter number 2:"))

mylist1 = []
mylist2 = []

for i in range (1,n1 + 1):
    if n1 % i == 0:
        mylist1.append(i)
    else:
        pass

for j in range (1,n2+1):
    if n2 % j == 0:
        mylist2.append(j)
    else:
        pass

common_elements_gcd = list(set(mylist1) & set(mylist2))

gcd = max(common_elements_gcd)

mylist1a = []
mylist2a = []

for a in range (1,101):
    product = n1 * a
    mylist1a.append(product)

for b in range (1,101):
    product2 = n2 * b
    mylist2a.append(product2)

common_elements_lcm = list(set(mylist1a) & set(mylist2a))

lcm = min(common_elements_lcm)

print("GCD: ", gcd)
print("LCM: ", lcm)
