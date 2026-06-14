string = input("Enter sentence: ")

clean1 = set(string.lower().replace(" ", ""))
alphabet = set('abcdefghijklmnopqrstuvwxyz')

common = clean1 & alphabet   # intersection of both sets

if len(common) == 26:
    print("Pangram! ✓ Contains all 26 letters")
else:
    print(f"Not a pangram ✗")
    print(f"Missing {26 - len(common)} letters")
