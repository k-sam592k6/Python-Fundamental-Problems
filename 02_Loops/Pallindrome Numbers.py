n1 = int(input("Enter start number: "))
n2 = int(input("Enter end number: "))

final_list = []

for i in range(n1, n2+1):
    if str(i) == str(i)[::-1]:
        final_list.append(i)

print(f"Palindrome numbers between {n1} and {n2}:")
print(*final_list)
print(f"Total found: {len(final_list)}")
