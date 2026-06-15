string = input("Enter word: ")

final = ""

for char in string:
    if char not in final:
        final += char 

print(final)
