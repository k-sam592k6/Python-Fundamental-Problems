cart = {}
discount = 0

while True:
    choice = int(input("\n1. Add item\n2. Remove item\n3. Apply discount\n4. Print receipt\n5. Exit\nChoice: "))

    if choice == 1:
        item_name = input("Item name: ")
        item_price = float(input("Price: "))
        cart[item_name] = item_price        # fixed

    elif choice == 2:
        remove_item = input("Item name: ")
        if remove_item in cart:             # fixed
            cart.pop(remove_item)
        else:
            print("Item not found!")

    elif choice == 3:
        discount = float(input("Enter discount %: "))

    elif choice == 4:
        subtotal = sum(cart.values())
        total = subtotal - (discount * 0.01) * subtotal
        print("\n------- Receipt -------")
        for item, price in cart.items():
            print(f"{item:15}: ₹{price:.2f}")
        print("-----------------------")
        print(f"Subtotal  : ₹{subtotal:.2f}")
        print(f"Discount  : {discount}%")
        print(f"Total     : ₹{total:.2f}")
        print("-----------------------")

    elif choice == 5:
        break
