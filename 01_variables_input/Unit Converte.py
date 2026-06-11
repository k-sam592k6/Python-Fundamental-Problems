def kmtomile(k):
    return k * 0.621371
def miletokm(m):
    return m * 1.6093
def kgtopound(w):
    return w * 2.20462
def poundtokg(p):
    return p * 0.45359
def litretogallon(l):
    return l * 0.264172
def gallontolitre(g):
    return g * 3.78541

print("1. km --> miles")
print("2. miles --> km")
print("3. kg --> pounds")
print("4. pounds --> kg")
print("5. litres --> gallons")
print("6. gallons --> litres")

choice = int(input("Enter choice(1,2,3,4,5,6): "))
value = float(input("Enter value: "))

if choice == 1:
    print(f"{value:.2f} km = {kmtomile(value):.2f} miles")
elif choice == 2:
    print(f"{value:.2f} miles = {miletokm(value):.2f} km")
elif choice == 3:
    print(f"{value:.2f} kg = {kgtopound(value):.2f} pounds")
elif choice == 4:
    print(f"{value:.2f} pounds = {poundtokg(value):.2f} kg")
elif choice == 5:
    print(f"{value:.2f} litres = {litretogallon(value):.2f} gallons")
elif choice == 6:
    print(f"{value:.2f} gallons = {gallontolitre(value):.2f} litres")
else:
    print("Invalid choice!")
