class UserInfo:
    def __init__(self, first_name, surname, mobile, account_owner_id):   # __init__ to assign values to objects 
        # arguments
        self.first_name = first_name
        self.surname = surname
        self.mobile = mobile
        self.account_owner_id = account_owner_id
    
    @classmethod
    def from_file(cls, file_path): # arguments being passed as parameters to 'from_file' 
        with open(file_path, 'r+') as f:    #with = o open and manage files.     # open(file_path, 'r+') = automatically close the file after being used.  # opens the file specified by file_path in read and write mode 'r+'.   #f = This variable can be used to interact with the file later on in the program
            lines = f.readlines()[1:]  # eads all lines from the file object, removes the first line, and returns the remaining lines as a list of strings, also skips the header in the txt files
            users = [] # creates list
            for line in lines:   # for loop.     line = variable assigned to each line in lines        in = iterate over 'lines'
                fields = line.strip().split(',') # fields = variable assigned to the sub strings                       line.split(','): This is a method that splits the string into a list of substrings
                if len(fields) < 3:    #len(fields) < 3 = checks if the line of text being processed is less then 3 
                    fields.extend(["N/A"] * (4 - len(fields))) # add default values for missing fields
                first_name, surname, mobile, account_owner_id = fields # assigns the values in the fields list to the variables 
                user = cls(first_name, surname, mobile, account_owner_id) # new instance of the UserInfo class and assigns it to the variable user.   # cls = current class 
                users.append(user) # adds each newly created user instance to the users list. By the end of the from_file method, the users list contains all the UserInfo 
        return users # returns the users list containing all the UserInfo
