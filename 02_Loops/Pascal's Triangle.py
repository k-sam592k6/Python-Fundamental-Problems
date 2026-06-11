from math import factorial

rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(1, rows - i):
        print(end="  ")         

    for r in range(i + 1):
        ncr = factorial(i) // (factorial(r) * factorial(i - r))
        print(f"{ncr:4}", end='')

    print()                      
