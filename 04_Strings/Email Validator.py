email = input("Enter email: ")

if " " in email:
    print("✗ Invalid! Spaces not allowed")
elif "@" not in email:
    print("✗ Invalid! Missing @")
elif email[0] == "@":
    print("✗ Invalid! @ can't be first character")
elif email[-1] == "@":
    print("✗ Invalid! @ can't be last character")
elif "." not in email[email.index("@"):]:
    print("✗ Invalid! No dot after @")
elif email[-1] == ".":
    print("✗ Invalid! Can't end with a dot")
else:
    print("✓ Valid email!")
