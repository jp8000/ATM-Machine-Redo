import pytest
from src.ATM_Machine.Get_Account_Types_and_Numbers import get_account_types_and_numbers
from src.ATM_Machine import Opening_Accounts_Data




def test_get_account_types_and_numbers():
    # creates a list of objects, each ojct contains AccountOwnerID, AccountNumber, AccountType, OpeningBalance
    accounts = [
        Opening_Accounts_Data.OpeningAccountData(1, "111111", "Cheque", 500),
        Opening_Accounts_Data.OpeningAccountData(2, "654321", "Savings", 1000),
        Opening_Accounts_Data.OpeningAccountData(3, "789012", "Cheque", 200),
        Opening_Accounts_Data.OpeningAccountData(1, "444444", "Savings", 1500),
    ]
    account_owner_id = 1.  # the value '1' is used as the input for the account ID number 
    expected_output = [("Cheque", "111111"), ("Savings", "444444")] # expected output for the values of accout_id_id = 1 
    assert get_account_types_and_numbers(accounts, account_owner_id) == expected_output # check that accounts, account_owner_id is equal to to the expected output 


# cd into "tests" folder
# command: python3 -m pytest -v test_Get_Account_Types_and_Numbers.py