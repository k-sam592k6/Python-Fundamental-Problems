balance  = 1000
print(f"Intial Balance {balance:.2f}")


print("Menu: ")

while choice != 4:
    choice = int(input(\
    "1. Check Balance " 
    "\n 2. Deposits " 
    "\n 3. Withdraw Money" 
    "\n 4. Exit"))

    if choice == 1:
        print(f"Current Balance {balance}")
    elif choice == 2:
        deposit = float(input("Deposit Amount: "))
        balance = deposit + balance
        print(f"Updated Balance: {balance:.2f}")
    elif choice == 3:
        withdraw = float(input("Withdraw Amount: "))
        if withdraw < balance :
            balance = balance - withdraw
            print(f"Updated Balance: {(balance):.2f}")
        else :
            print("Insufficient Balance")
    elif choice == 4:
        print("Have a nice day!!")
        break
    else:
        print("Invalid Choice")
