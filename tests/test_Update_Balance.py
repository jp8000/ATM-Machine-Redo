import os
import pytest 

from src.ATM_Machine.Update_Balance import update_balance_file


def test_update_balance_file():
    # Create test data with some initial data
    test_file_path = 'test_balances.txt'
    with open(test_file_path, 'w') as f:
        f.write('001|||9264945|||Cheque|||250\n')
        f.write('002|||9676422|||Saving|||100\n')

    # Update the balance for 001 account id number
    update_balance_file(test_file_path, '9264945', "500")

    # Check that the file was updated correctly
    with open(test_file_path, 'r') as f:
        lines = f.readlines()
        assert lines[0] == '001|||9264945|||Cheque|||500\n'
        assert lines[1] == '002|||9676422|||Saving|||100\n'

    # Clean up the test file
    os.remove(test_file_path)



# cd into "tests" folder
# command: python3 -m pytest -v test_Update_Balance.py