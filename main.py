import os

isloggedin = False

login_option = input("(1) Logging in\n(2) Creating a new account:\n>----------------------------<\n ")

def vault():
    global user
    user = input("Enter your username: ")
    pw = input("Enter your password: ")
    global directory
    directory = '.\\info\\' + user + "\\"

    try:
        with open(directory + user, "r") as fp:
            checkuser = fp.read()
            fp.close
        # checking for proper username
        if checkuser != user:
            print("Incorrect username or password. Try again.")
            vault()
    except:
        print("Incorrect username or password. Try again.")
        vault()

    pwname = "MASTERpass" + user
    with open(directory + pwname, 'r') as fp:
        checkpw = fp.read()

    if checkpw == pw:
        print("Welcome to your password vault, " + user + "!")
        c_or_v = input("Vault\n>-----------------<\n(1) Create a new account\n(2) View accounts:\n")
        if c_or_v == '1':
            user_create_acc()
        if c_or_v == '2':
            user_view_accs()



def user_create_acc():
    global user
    instance_name = input("Enter the name of this account: ")

    directory = ".\\info\\" + user + "\\accounts\\"

    # makes initial account folder if not already there
    isExist = os.path.exists(directory)
    if isExist == False:
        os.mkdir(directory)


    directory = ".\\info\\" + user + "\\accounts\\" + instance_name + "\\"
    os.mkdir(directory)

    instance_user = input("Account Creation\n>-----------<\nUsername: ")
    instance_pass = input("Password: ")

    with open(directory + instance_user, 'a') as fp:
        fp.write(instance_user)
        fp.close

    name = "pass" + instance_user
    with open(directory + name, 'a') as fp:
        fp.write(instance_pass)
    print("Account created! Log back in, please!\n\n\n")
    vault()



def user_view_accs():
    global user
    directory = ".\\info\\" + user + "\\accounts\\"

    x = os.listdir(directory)
    print(x)
    account_pick = input("\n\n\nType the name of the account you'd like to access (Must be exact, without brackets or apostrophes): ")
    directory = directory + account_pick + "\\"
    x = os.listdir(directory)
    usernamedir = directory + x[0]
    passwordNamedir = directory + x[1]

    try:
        with open(usernamedir, 'r') as fp:
            username = fp.read()
            fp.close()
        with open(passwordNamedir, 'r') as fp:
            password = fp.read()
            fp.close
    except:
        print("Did you type the name incorrectly? Try again.")
        user_view_accs()
    print("Username: " + username + "\nPassword: " + password)







def master_create():
    master_create_user = input("Enter your desired MASTER username: ")
    master_create_pass = input("Enter your desired MASTER password: ")

    try:
        directory = '.\\info\\' + master_create_user + "\\"
        os.mkdir(directory)

    except:
        print("No info file created. Creating now..")
        os.mkdir('.\\info\\')
        master_create()


    with open(directory + master_create_user, 'a') as fp:
        fp.write(master_create_user)
        fp.close()

    name = "MASTERpass" + master_create_user
    with open(directory + name, 'a') as fp:
        fp.write(master_create_pass)
        fp.close

    logqm = input("Login credentials created! \n"
                  "Would you like to log in? (y/n):")
    if logqm == "y":
        vault()
    else:
        exit()

if login_option in ["1"]:
    print("\n")
    vault()

if login_option in ["2"]:
    print("\n")
    master_create()

