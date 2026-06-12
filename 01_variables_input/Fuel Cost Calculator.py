distance = float(input("Distance(km) :"))
efficiency = float(input("Eficiency (km/l): "))
fuelprice = float(input("Fuel Price per Litre: "))

if efficiency == 0:
    print("Efficiency cannot be 0")
else:
    print(f"Fuel Needed: {(distance/efficiency):.2f}L")
    print(f"Total Fuel Cost: {((distance/efficiency) * fuelprice):.2f}")
