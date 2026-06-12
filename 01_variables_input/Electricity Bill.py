def first100units(u):
    return u * 1.5
def next101_200units(u):
    return u * 2.5
def morethan200units(u):
    return u * 3.5

units = int(input("Units Consumed: "))
print("Bill Breakdown:")

if units <= 100:
    print(f"First {units} units    : ₹{first100units(units):.2f} (₹1.5/unit)")
    print(f"Total Bill            : ₹{first100units(units):.2f}")

elif units <= 200:
    next_units = units - 100
    total = (100*1.5) + next101_200units(next_units)
    print(f"First 100 units       : ₹{100*1.5:.2f} (₹1.5/unit)")
    print(f"Next {next_units} units        : ₹{next101_200units(next_units):.2f} (₹2.5/unit)")
    print(f"Total Bill            : ₹{total:.2f}")

else:
    remaining = units - 200
    total = (100*1.5) + (100*2.5) + morethan200units(remaining)
    print(f"First 100 units       : ₹{100*1.5:.2f} (₹1.5/unit)")
    print(f"Next 100 units        : ₹{100*2.5:.2f} (₹2.5/unit)")
    print(f"Remaining {remaining} units   : ₹{morethan200units(remaining):.2f} (₹3.5/unit)")
    print(f"Total Bill            : ₹{total:.2f}")
