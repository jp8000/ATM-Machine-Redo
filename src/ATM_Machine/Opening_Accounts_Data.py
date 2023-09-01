class OpeningAccountData:
    def __init__(self, account_owner_id, account_number, account_type, opening_balance):
        self.account_owner_id = account_owner_id
        self.account_number = account_number
        self.account_type = account_type
        self.opening_balance = opening_balance
    
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r+') as f:
            lines = f.readlines()[1:] 
            accounts = []
            for line in lines:
                fields = line.strip().split('|||')
                account_owner_id, account_number, account_type, opening_balance = fields
                account = cls(account_owner_id, account_number, account_type, opening_balance)
                accounts.append(account)
        return accounts