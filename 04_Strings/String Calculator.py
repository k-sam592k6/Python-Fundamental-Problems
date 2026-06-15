mylist = input("Enter expression: ").split()

num1 = float(mylist[0])
op   = mylist[1]
num2 = float(mylist[2])

if op == "+":
    print(f"Result: {num1} + {num2} = {num1 + num2:.1f}")
elif op == "-":
    print(f"Result: {num1} - {num2} = {num1 - num2:.1f}")
elif op == "*":
    print(f"Result: {num1} X {num2} = {num1 * num2:.1f}")
elif op == "/":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print(f"Result: {num1} / {num2} = {num1 / num2:.1f}")
else:
    print("Operation can't be performed!")
