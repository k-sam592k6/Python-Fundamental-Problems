s1 = input("Enter string 1: ")

s2 = input("Enter string 2: ")

if len(s1) != len(s2):
    print("Lengths dont match thus rotations is not possible")
else:
    if s2 in (s1 + s1):
        print("Second string is the rotation of First String")
    else:
        print("Second string is not a rotation of the first string")
