def agecalulator(year):
    return 2026 - year
birth_year = int(input("Enter your birth year:"))
age = agecalulator(birth_year)
if agecalulator(age) >= 18:
    print(f"Age: {age}")
    print("Eligible to vote")
    print("Years to retirement: ", 60 - agecalulator(age))
elif agecalulator(age) < 18 :
    print(f"Age: {age}")
    print("Not eligible to vote")
    print("Years to retirement: ", 60 - agecalulator(age))
else:
    print("Invalid Age")
