s = input("Enter string: ")
mylist = [c.lower() for c in s if c.isalnum()]

if mylist == mylist[::-1]:
    print("Valid palindrome")
else:
    print("Not a valid palindrome")
