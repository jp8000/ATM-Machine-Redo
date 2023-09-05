def get_account_types_and_numbers(accounts, account_owner_id):  # function is used to fetch the user's accounts 
    account_types_and_numbers = []
    for account in accounts:
        if account.account_owner_id == account_owner_id:      # if 'account.account_owner_id' matches the 'account_owner_id' 
            account_types_and_numbers.append((account.account_type, account.account_number)) # creates a list of tuples, each tuple contains the account type and account number 
    return account_types_and_numbers # retuns the account_types_and_numbers when the function is called 

