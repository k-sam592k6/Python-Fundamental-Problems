bill = float(input("Enter bill amount: "))
tip_ptage = float(input("Enter tip percentage: "))
npeople = int(input("Number of people: "))

tip_amount = bill * (tip_ptage / 100)
total_bill = bill + tip_amount

print("---------------------------------")
print(f"Bill Amount      : {bill:.2f}")
print(f"Tip%             : {tip_ptage}%")
print(f"Tip Amount       : {tip_amount:.2f}")
print(f"Total Bill       : {total_bill:.2f}")
print(f"Each Person Pays : {total_bill / npeople:.2f}")
print("---------------------------------")
