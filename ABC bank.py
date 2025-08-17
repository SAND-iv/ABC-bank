# Initializing vAriables
customers = []
bank_balance = 0.0
account_number=0
nic=0
first_name=0
last_name=0
birth_date=0
permanent_address=0
phone_number=0

# Main loop
while True:
    print("ABC Bank".center(75))
    print("Main Menu".center(75))
    print("1. Add a new customer")
    print("2. View details of a customer including his/her bank balance")
    print("3. View details of all the customers with their bank balances")
    print("4. Deposit money to a given account ")
    print("5. Withdraw money from a given account ")
    print("6. Update customer details")
    print("7. Exit")

    if 'choice' not in locals():
        choice = input("                                your choice: ")

    if choice == '1':
        # Add a new customer
        print("ABC Bank".center(75))
        print("Add a new customer".center(75))
        if len(customers) < 5:
            account_number = input("Enter 10-digit account number: ")
            while len(account_number) != 10 or not account_number.isdigit():
                account_number = input("Invalid input. Enter a 10-digit account number: ")

            nic = input("NIC (10 characters): ")
            while len(nic) != 10:
                nic = input("Invalid input. Enter NIC (10 characters): ")

            first_name = input("Enter First Name (max 10 characters): ")
            while len(first_name) >= 10:
                first_name = input("Invalid input. Enter First Name (max 10 characters): ")

            last_name = input("Enter Last Name (max 15 characters): ")
            while len(last_name) >= 15:
                last_name = input("Invalid input. Enter Last Name (max 15 characters): ")

            birth_date = input("Birth Date (YYYY.MM.DD): ")
            while len(birth_date) != 10:
                birth_date = input("Invalid input. Enter birth date (YYYY.MM.DD): ")

            permanent_address = input("Enter your permanent address (max 15 characters): ")
            while len(permanent_address) >= 15:
                permanent_address = input("Invalid input. Enter your permanent address (max 15 characters): ")

            phone_number = input("Phone Number (10 characters): ")
            while len(phone_number) != 10:
                phone_number = input("Invalid input. Enter phone number (10 characters): ")

            #Saving the account
            save_account = input("Do you want to save the account (Yes/No)? ").strip().lower()
            if save_account == 'yes':
                new_customer = {
                    'account_number': account_number,
                    'nic': nic,
                    'first_name': first_name,
                    'birth_date': birth_date,
                    'last_name': last_name,
                    'permanent_address': permanent_address,
                    'phone_number': phone_number,
                    'bank_balance': bank_balance
                }
                customers.append(new_customer)
                print(f"Customer {first_name} {last_name} added successfully.")
            else:
                print("Customer account not saved.")
        else:
            print("Maximum customer limit reached (5 customers).")
        del choice

    elif choice == '2':
        # View customer details
        print("ABC Bank".center(75))
        print("View details of a customer".center(75))
        while True:
            account_number = input("Enter account number to view details: ")
            customer_found = False
            for customer in customers:
                if customer['account_number'] == account_number:
                    print(f"NIC: {customer['nic']}")
                    print(f"Phone Number: {customer['phone_number']}")
                    print(f"First Name: {customer['first_name']}")
                    print(f"Last Name: {customer['last_name']}")
                    print(f"Bank Balance: {customer['bank_balance']} LKR")
                    customer_found = True
                    break
            if not customer_found:
                print("Customer not found.")
            
            another = input("Do you want to view another account details (Yes/No)? ").strip().lower()
            if another != 'yes':
                break
        del choice

    elif choice == '3':
        # Display all customers
        print("ABC Bank".center(75))
        print("View details of all customer".center(75))
        if not customers:
            print("No customers registered yet.")
        else:
            print("List of Customers:")
            for customer in customers:
                print("--------------------")
                print(f"NIC: {customer['nic']}")
                print(f"Account Number: {customer['account_number']}")
                print(f"First Name: {customer['first_name']}")
                print(f"Last Name: {customer['last_name']}")
                print(f"Bank Balance: {customer['bank_balance']} LKR")
            
            update_account = input("Do you want to update the account details (Yes/No)? ").strip().lower()
            if update_account == 'yes':
                choice = '6'
                continue
            else:
                del choice

    elif choice == '4':
        # Deposit money
        print("ABC Bank".center(75))
        print("Deposit Money to a given account".center(75))
        account_number = input("Bank Account Number: ")
        amount = float(input("Deposit Amount: "))
        customer_found = False
        for customer in customers:
            if customer['account_number'] == account_number:
                confirm_deposit = input(f"Do you want to save(Yes/No)? ").strip().lower()
                if confirm_deposit == 'yes':
                    customer['bank_balance'] += amount
                    print(f"Deposited {amount} LKR. New balance: {customer['bank_balance']} LKR")
                else:
                    print("Deposit not saved.")
                customer_found = True
                break
        if not customer_found:
            print("Customer not found.")
        del choice

    elif choice == '5':
        # Withdraw money
        print("ABC Bank".center(75))
        print("Withdraw money from a given account".center(75))
        account_number = input("Bank Account Number: ")
        amount = float(input("Withdraw Amount: "))
        customer_found = False
        for customer in customers:
            if customer['account_number'] == account_number:
                if customer['bank_balance'] >= amount:
                    confirm_withdraw = input(f"Do you want to save(Yes/No)? ").strip().lower()
                    if confirm_withdraw == 'yes':
                        customer['bank_balance'] -= amount
                        print(f"Withdrew {amount} LKR. New balance: {customer['bank_balance']} LKR")
                    else:
                        print("Withdrawal not saved.")
                else:
                    print("Insufficient balance!")
                customer_found = True
                break
        if not customer_found:
            print("Customer not found.")
        del choice

    elif choice == '6':
        # Update customer details
        print("ABC Bank".center(75))
        print(" Update Customer Details ".center(75))
        account_number = input("Bank Account Number: ")
        customer_found = False
        for customer in customers:
            if customer['account_number'] == account_number:
                print(f"Updating details for {customer['first_name']} {customer['last_name']}:")
                
                new_nic = input(f"Enter new NIC (10 characters, current: {customer['nic']}): ")
                if new_nic:
                    while len(new_nic) != 10:
                        new_nic = input("Invalid input. Enter new NIC (10 characters): ")
                    customer['nic'] = new_nic

                new_first_name = input(f"Enter new First Name (max 10 characters, current: {customer['first_name']}): ")
                if new_first_name:
                    while len(new_first_name) > 10:
                        new_first_name = input("Invalid input. Enter new First Name (max 10 characters): ")
                    customer['first_name'] = new_first_name

                new_last_name = input(f"Enter new Last Name (max 15 characters, current: {customer['last_name']}): ")
                if new_last_name:
                    while len(new_last_name) > 15:
                        new_last_name = input("Invalid input. Enter new Last Name (max 15 characters): ")
                    customer['last_name'] = new_last_name

                new_birth_date = input(f"Enter new Birth Date (YYYY.MM.DD, current: {customer['birth_date']}): ")
                if new_birth_date:
                    while len(new_birth_date) != 10:
                        new_birth_date = input("Invalid input. Enter new Birth Date (YYYY.MM.DD): ")
                    customer['birth_date'] = new_birth_date

                new_permanent_address = input(f"Enter new Permanent Address (max 15 characters, current: {customer['permanent_address']}): ")
                if new_permanent_address:
                    while len(new_permanent_address) > 15:
                        new_permanent_address = input("Invalid input. Enter new Permanent Address (max 15 characters): ")
                    customer['permanent_address'] = new_permanent_address

                new_phone_number = input(f"Enter new Phone Number (10 characters, current: {customer['phone_number']}): ")
                if new_phone_number:
                    while len(new_phone_number) != 10:
                        new_phone_number = input("Invalid input. Enter new Phone Number (10 characters): ")
                    customer['phone_number'] = new_phone_number

                # Confirm saving the new details
                save_details = input("Do you want to save the new details (Yes/No)? ").strip().lower()
                if save_details == 'yes':
                    print("Customer details updated successfully.")
                else:
                    print("Customer details not updated.")
                customer_found = True
                break
        if not customer_found:
            print("Customer not found.")
        del choice

    elif choice == '7':
        # Exit the program
        print("Exiting ABC Bank Management System. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
        del choice
