def emi(p,r,n):
    rate = (r/12) * 0.01
    return (p * rate * ((1+rate)**n)) / ((1+rate)**n - 1)

loan_amount = float(input("Enter loan amount              : "))
interest_rate = float(input("Enter annual interest rate(%): "))
tenure = int(input("Enter tenure(months)                  : "))
monthly_payment = emi(loan_amount, interest_rate, tenure)

print(f"Loan Amount: {loan_amount:.2f}")
print(f"Interest Rate: {interest_rate:.1f}% per annum")
print(f"Tenure: {tenure} months")
print(f"Monthly EMI: {monthly_payment:.2f}")
print(f"Total Payment: {(monthly_payment * tenure):.2f}")
print(f"Total interest: {((monthly_payment * tenure) - loan_amount):.2f}")
