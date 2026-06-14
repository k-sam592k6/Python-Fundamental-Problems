word1 = input("Enter string 1: ")
word2 = input("Enter string 2: ")

clean1 = sorted(word1.lower().replace(" ", ""))
clean2 = sorted(word2.lower().replace(" ", ""))

if clean1 == clean2:
    print(f'"{word1}" and "{word2}" are anagrams! ✓')
else:
    print(f'"{word1}" and "{word2}" are not anagrams! ✗')
