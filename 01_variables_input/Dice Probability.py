sides = int(input("Enter number of sides: "))
target = int(input("Enter target number: "))

probability = 1/sides
percentage = probability * 100

if target > sides :
    print("Target number doesn't exit on this dice!")
elif target < 1:
    print("Invalid target number!")
else:
    print(f"Target number: {target}")
    print(f"Sides on dice: {sides}")
    print(f"Probability: {probability}")
    print(f"In Percentage: {percentage:.2f}%")
