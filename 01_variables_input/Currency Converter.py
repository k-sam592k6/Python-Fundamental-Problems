def inr_to_usd(inr):
    return inr * 0.0104
def inr_to_eur(inr):
    return inr * 0.0090
def inr_to_gbp(inr):
    return inr * 0.0078
def usd_to_inr(usd):
    return usd * 95.38
def eur_to_inr(eur):
    return eur * 110.28
def gbp_to_inr(gbp):
    return gbp * 127.66

print("Select Conversion")
print("1. INR --> USD \n 2. INR --> EUR \n 3. INR --> GBP \n 4. USD --> INR \n 5. EUR --> INR \n 6. GBP --> INR" )

choice = int(input("Enter choice: "))
amount = float(input("Enter amount: "))

if choice == 1:
    print(f"₹{amount:.2f} = ${inr_to_usd(amount):.2f}")
elif choice == 2:
    print(f"₹{amount:.2f} = €{inr_to_eur(amount):.2f}")
elif choice == 3:
    print(f"₹{amount:.2f} = £{inr_to_gbp(amount):.2f}")
elif choice == 4:
    print(f"${amount:.2f} = ₹{usd_to_inr(amount):.2f}")
elif choice == 5:
    print(f"€{amount:.2f} = ₹{eur_to_inr(amount):.2f}")
elif choice == 6:
    print(f"£{amount:.2f} = ₹{gbp_to_inr(amount):.2f}")
else :
    print("Invalid Choice")
