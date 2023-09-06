# Function is used to fetch the user's accounts 
def get_account_types_and_numbers(accounts, account_owner_id):  
    account_types_and_numbers = []
    for account in accounts:
        if account.account_owner_id == account_owner_id:      # If 'account.account_owner_id' matches the 'account_owner_id' 
            account_types_and_numbers.append((account.account_type, account.account_number)) # Creates a list of tuples, each tuple contains the account type and account number 
    return account_types_and_numbers # Retuns the account_types_and_numbers when the function is called 

