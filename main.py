import random, string 

try_again = True

while try_again:
    
    pass_len = int(input("Enter length of password: "))
    pass_type = int(input("What type of password? (Enter digit 1-4)\n1.) Only uppercase\n2.) Only lowercase\n3.) Only numbers\n4.) Only symbols\n5.) Mixed/Doesn't matter\n"))
    password = ''

    # generates uppercase ascii passwords only
    if pass_type == 1:
        for x in range(pass_len):
            password += random.choice(string.ascii_uppercase)
        print(password)
        
    # generates lowercase ascii passwords only
    elif pass_type == 2:
        for x in range(pass_len):
            password += random.choice(string.ascii_lowercase)
        print(password)
        
    # generates numeric passwords only
    elif pass_type == 3:
        for x in range(pass_len):
            password += random.choice(string.digits)
        print(password)
        
    # generates symbolic passwords only
    elif pass_type == 4:
        for x in range(pass_len):
            password += random.choice(string.punctuation)
        print(password)
        
    # generates mixed password (lowercase, uppercase, numbers, symbols)
    elif pass_type == 5:
        for x in range(pass_len):
            password += random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)
        print(password)
    else:
        print("Try again.")
    
    try_again = input("Would you like to generate another password? (y/n) ")
    if try_again == "y":
        continue
    else:
        break
