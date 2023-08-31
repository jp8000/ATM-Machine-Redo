def print_account_summary(account_types_and_numbers, accounts):
    print("Please find your account summary below:")
    for i, (account_type, account_number) in enumerate(account_types_and_numbers):
        for acc in accounts:
            if acc.account_type == account_type and acc.account_number == account_number:
                print(f"{i+1}. Account Type:{account_type}   Account Number:{account_number}   Account Balance:{acc.opening_balance}")
                continue
                # print_account_summary(account_types_and_numbers, accounts)