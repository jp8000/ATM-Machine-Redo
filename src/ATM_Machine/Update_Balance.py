def update_balance_file(file_path, account_number, new_balance):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    with open(file_path, 'w') as f:
        for line in lines:
            fields = line.strip().split('|||')
            if fields[1] == account_number:
                fields[3] = str(new_balance)
                line = '|||'.join(fields) + '\n'
            f.write(line)
