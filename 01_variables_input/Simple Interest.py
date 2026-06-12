def interest(p,r,t):
    return (p*r*t)/100

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time(years) :"))

si = interest(principal, rate, time)
total_amount = principal+si

print(f"Principal: {principal:.2f}")
print(f"Rate: {rate}%")
print(f"Time: {time} years")
print(f"Simple Interest: {si:.2f}")
print(f"Total Amount: {total_amount:.2f}")
