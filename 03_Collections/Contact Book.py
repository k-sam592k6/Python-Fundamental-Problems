call_dict = {}

while True:
    choice = int(input("1. Add contact " \
                       "\n 2. Delete Contact \n" \
                       "3. Search contact \n" \
                       "4. Print all contacts \n" \
                       "5. Exit"))
    
    if choice == 1:
        name = str(input("Name: "))
        phone_number = (input("Number: "))

        call_dict[name] = phone_number

    elif choice == 2:
        delete_name = str(input("Name: "))
        if delete_name in call_dict:
            call_dict.pop(delete_name)
        else:
            print("Contact Doesnt exist")

    elif choice == 3:
        search_name = str(input("Search: "))
        if search_name in call_dict:
            print(f"{search_name}: {call_dict[search_name]}")
        else:
            print("Contact not found")

    elif choice == 4:
        for name in sorted(call_dict):
            print(f"{name:15}: {call_dict[name]}")

    elif choice == 5:
        break
