def bmi(w, h):
    return w / (h ** 2)

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

result = bmi(weight, height)

print(f"\nBMI: {result:.2f}")

if result < 18.5:
    print("Category: Underweight")
    print("Status: You are below the healthy range")
elif result < 25:
    print("Category: Normal Weight")
    print("Status: You are in a healthy range ✓")
elif result < 30:
    print("Category: Overweight")
    print("Status: You are above the healthy range")
elif result < 35:
    print("Category: Obese Class 1")
    print("Status: High health risk")
elif result < 40:
    print("Category: Obese Class 2")
    print("Status: Very high health risk")
else:
    print("Category: Obese Class 3")
    print("Status: Extremely high health risk")
