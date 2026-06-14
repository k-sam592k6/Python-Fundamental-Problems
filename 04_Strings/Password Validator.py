password = input("Enter password: ")

errors = []

if not any(c.isupper() for c in password):
    errors.append("Uppercase letter missing")
if not any(c.islower() for c in password):
    errors.append("Lowercase letter missing")
if not any(c.isdigit() for c in password):
    errors.append("Digit missing")
if not any(c in "!@#$%^&*" for c in password):
    errors.append("Special character missing")
if len(password) < 8:
    errors.append(f"Too short ({8-len(password)} more chars needed)")

if len(errors) == 0:
    print("Password is strong! ✓")
else:
    print("Password is weak! ✗")
    for error in errors:
        print(f"  ✗ {error}")
