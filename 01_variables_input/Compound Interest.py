def interest(p,r,n,t):
    return p*(1+ ((0.01*r)/n))**(n*t)

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (years): "))
compounding_frequency = float(input("Enter compounding frequence (per year): "))

total_amount = interest(principal, rate, compounding_frequency, time)
ci = total_amount - principal

print(f"Principal: {principal:.2f}")
print(f"Rate: {rate}%")
print(f"Time: {time} years")
print(f"Compound: {compounding_frequency} times/year")
print(f"Total Amount: {total_amount:.2f}")
print(f"Compound Interest: {ci:.2f}")
