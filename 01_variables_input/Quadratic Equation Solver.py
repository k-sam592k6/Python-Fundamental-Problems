import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

dis = b**2 - (4*a*c)

print("---------------------------------")
if dis > 0:
    sq = math.sqrt(dis)
    root1 = (-b + sq) / (2*a)
    root2 = (-b - sq) / (2*a)
    print(f"Root 1 : {root1:.2f}")
    print(f"Root 2 : {root2:.2f}")
elif dis == 0:
    root = -b / (2*a)
    print(f"One root: {root:.2f}")
else:
    print("No real roots exist")
print("---------------------------------")
