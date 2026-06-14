string = input("Enter string: ")

vowelslist = []
consonants = []
digits = []
spaces = []
other = []

vowels = "aeiouAEIOU"

for char in string:
    if char in vowels:
        vowelslist.append(char)
    elif char.isalpha():
        consonants.append(char)
    elif char.isdigit():
        digits.append(char)
    elif char == " ":
        spaces.append(char)
    else:
        other.append(char)

print(f"Vowels     : {len(vowelslist)}")
print(f"Consonants : {len(consonants)}")
print(f"Digits     : {len(digits)}")
print(f"Spaces     : {len(spaces)}")
print(f"Other      : {len(other)}")
