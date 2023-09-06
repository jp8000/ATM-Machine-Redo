import pytest

from src.ATM_Machine.Account_Summary import print_account_summary
from src.ATM_Machine import Opening_Accounts_Data



def test_print_account_summary(capfd):
    # Create test data for the test
    account_types_and_numbers = [("Cheque", "9264945"), ("Savings", "9676422")]
    accounts = [Opening_Accounts_Data.OpeningAccountData(1, "9264945", "Cheque", 1000), Opening_Accounts_Data.OpeningAccountData(2, "9676422", "Savings", 5000)]

    # Call function with test data
    print_account_summary(account_types_and_numbers, accounts)

    # Capture output
    captured = capfd.readouterr()   # This is a fixture from the pytest used to capture the output strean of print_account_summary
    output_lines = captured.out.strip().split('\n')  # Strip() = used to remove white/empty space from the string to unsure the comparison to the output in not affected 
                                                     # Split() = used to split the sting into lines, this is because the expected output is also displaying to split lines 

    # Check if output matches expected output
    assert len(output_lines) == 3     # == 3  = checks the numbers of lines captured is equal to 3 
    assert output_lines[0] == "Please find your account summary below:"
    assert output_lines[1] == "1. Account Type:Cheque   Account Number:9264945   Account Balance:1000"
    assert output_lines[2] == "2. Account Type:Savings   Account Number:9676422   Account Balance:5000"

# cd into "tests" folder
# Command python3 -m pytest -v test_Account_Summary.py