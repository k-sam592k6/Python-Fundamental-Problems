name = input("Enter name: ").split()

result = []

for word in name:
    result.append(word[0] + " ")

result.pop()
result.append(name[len(name) - 1])
print(*result)

