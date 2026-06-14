words = input("Enter words (space separated): ").split()

prefix = ""

for i in range(len(words[0])):
    char = words[0][i]
    
    match = True
    for word in words[1:]:
        if i >= len(word) or word[i] != char:
            match = False
            break
    
    if match:
        prefix += char
    else:
        break

if prefix == "":
    print("No common prefix found!")
else:
    print(f'Longest common prefix: "{prefix}"')
