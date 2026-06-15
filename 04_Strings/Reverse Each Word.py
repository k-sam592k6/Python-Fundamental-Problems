sentence = input("Enter sentence: ").split()

final = ""
for word in sentence:
    final += word[::-1] + " "

print(final)
