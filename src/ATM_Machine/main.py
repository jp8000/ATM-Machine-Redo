from Account_Summary import print_account_summary
from Get_Account_Types_and_Numbers import get_account_types_and_numbers
from Opening_Accounts_Data import OpeningAccountData
from Update_Balance import update_balance_file
from User_Info import UserInfo


users = UserInfo.from_file("data/UserInfo.txt") #creates a list of UserInfo objects by calling the from_file class method of the UserInfo class.
accounts = OpeningAccountData.from_file("data/OpeningAccountsData.txt") #creates a list of OpeningAccountData objects by calling the from_file class method of the OpeningAccountData class.




updates = [] # caputes the new balances but doesnt update

while True:
    # Ask the user to input their ID number
    user_id_number = input("Please enter your ID number: ")

    # Check if the user's ID number matches the account owner ID
    matched = False
    for user in users:
        if user_id_number == user.account_owner_id:
            print(f"Welcome {user.first_name} {user.surname}! Please select an option: 1, 2, 3, or q.")
            matched = True
            

    if not matched:
        print("Your ID number is incorrect, please try again!")
        continue
    # if the user's ID number does not match send user to start

    # Menu options
    banking_options = {
        '1': 'Deposit',
        '2': 'Withdraw',
        '3': 'Balance',
        'q': 'Quit'
    }

    
    # assigning the menu item a key and value
    print("Please select an option: ")
    for key, value in banking_options.items():
        print(f"{key}: {value}")

    # storing the user choice inside user choice
    user_choice = input("Select from the menu: ")

    # valid input check for the menu 
    if user_choice not in banking_options:
        print("Wrong input - Please make sure to enter a valid input.")
        continue



    # Process the user's choice to select an option
    if user_choice == "1": #DEPOSIT
        account_types_and_numbers = get_account_types_and_numbers(accounts, user_id_number)
        print("Which account do you wish to deposit into: ")
        for i, (account_type, account_number) in enumerate(account_types_and_numbers):
            print(f"{i+1}. {account_type}: {account_number}")

        # Get the user's choice of bank account
        account_choice = int(input("Select an account: "))
        if account_choice >= 1 and account_choice <= len(account_types_and_numbers):
    
            # Get the deposit amount from the user
            try:
                deposit_amount = float(input("Enter the amount you wish to deposit: "))
                print("You entered a deposit amount of:", deposit_amount)
            # Error check - If the users input is unable to be converted to an integer it means the input was invalid  
            except ValueError:
                print("Invalid deposit amount. Please enter a valid number.")
                continue

            # Find the selected account and update its balance
            for i, (account_type, account_number) in enumerate(account_types_and_numbers):
                if i+1 == account_choice:
                    for account in accounts:
                        if account.account_number == account_number:
                            account.opening_balance = str(float(account.opening_balance) + deposit_amount)

                            # prints the account plus the new opening balance
                            print(f"Deposit successful! The new balance for account {account_number} is {account.opening_balance}")
                            # Update the balance in the account object
                            account.opening_balance = str(float(account.opening_balance))

                            # add update to the updates list
                            update = (account.account_number, account.opening_balance)
                            updates.append(update)

                            # Prints selected account infomation 
                            print_account_summary(account_types_and_numbers, accounts)
            continue


    elif user_choice == "2": # WITHDRAW
        account_types_and_numbers = get_account_types_and_numbers(accounts, user_id_number)
        print("Which account do you wish to withdraw from: ")
        for i, (account_type, account_number) in enumerate(account_types_and_numbers):
            print(f"{i+1}. {account_type}: {account_number}")

        # Get the user's choice of bank account
        account_choice = int(input("Select an account: "))
        if account_choice >= 1 and account_choice <= len(account_types_and_numbers):
        
            # Get the Withdraw amount from the user
            try:
                withdraw_amount = float(input(f"Enter the amount you wish to withdraw: "))
                print("You entered a withdraw amount of:", withdraw_amount )
            # Error check - If the users input is unable to be converted to an integer it means the input was invalid  
            except ValueError:
                    print("Invalid deposit amount. Please enter a valid number.")
                    continue

            # Find the selected account and update its balance
            for i, (account_type, account_number) in enumerate(account_types_and_numbers):
                if i+1 == account_choice:
                    for account in accounts:
                        if account.account_number == account_number:
                            # checks if the user withdraw amount is greater then the current opening balance 
                            if withdraw_amount > float(account.opening_balance):
                                print(f"Error - Amount entered {withdraw_amount} which is greater than amount in account")

                            else:
                                # Takes the opening balance subtracts the users Withdraw amount 
                                account.opening_balance = str(float(account.opening_balance) - withdraw_amount)
                                print(f"The new balance for account {account_number} is {account.opening_balance}")
                                # Updates the balance in the account object
                                account.opening_balance = str(float(account.opening_balance))

                                # add update to the updates list
                                update = (account.account_number, account.opening_balance)
                                updates.append(update)

                                # Prints selected account infomation 
                                print_account_summary(account_types_and_numbers, accounts)
            continue
                        
                            



    elif user_choice  == "3":# BALANCE
        account_types_and_numbers = get_account_types_and_numbers(accounts, user_id_number)
        print("Which account do you wish to check the balance of: ")
        for i, (account_type, account_number) in enumerate(account_types_and_numbers):
            print(f"{i+1}. {account_type}: {account_number}")

        # Get the user's choice of bank account
        account_choice = int(input("Select an account: "))
        if account_choice >= 1 and account_choice <= len(account_types_and_numbers):


            # Find the selected account and update its balance
            for i, (account_type, account_number) in enumerate(account_types_and_numbers):
                if i+1 == account_choice:
                    for account in accounts:
                        if account.account_number == account_number:
                            # Prints the account type and account plus the opening balance
                            print(f"The opening balanmce of account ({account_type} - {account_number}) = {account.opening_balance}")
                            # Prints selected account infomation 
                            print_account_summary(account_types_and_numbers, accounts)
                continue
                    


    
    elif user_choice == "q":
        
        # update the balance in the file
        for update in updates:
            update_balance_file('data/OpeningAccountsData.txt', update[0], update[1])
        
        #reads OpeningAccountData.txt and stores the data inide accounts
        accounts = OpeningAccountData.from_file("data/OpeningAccountsData.txt")
        # A for loop which iterates each 'account' inside 'accounts' and prints the results 
        # The last print statement is empty to provide a space between each account for better readability
        for account in accounts:
            print("Account name: ", account.account_owner_id)
            print("Account type: ", account.account_type)
            print("Account number: ", account.account_number)
            print("Balance:", account.opening_balance)
            print()
        break # ends the program



    
# User will now loop back to the start of the program as it's a while loop 
    