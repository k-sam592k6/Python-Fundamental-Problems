data1 = input("Enter list 1 (space separated): ")
data2 = input("Enter list 2 (space separared): ")

list1 = data1.split()
list2 = data2.split()


pair = []
for i in range(min(len(list1), len(list2))):
    pair.append((list1[i], list2[i]))

print(*pair)

diff = abs(len(list1) - len(list2))
if diff > 0:
    longer = "list1" if len(list1) > len(list2) else "list2"
    print(f"\n Note: {diff} element(s) from {longer} were unpaired")
