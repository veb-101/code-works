#!/usr/bin/python3

# USER LOGIN PART =====================================================


def login():
    print("Welcome!!!!")
    wrong = False
    while not wrong:
        name = input("Enter Your First Name:")
        password = getpass.getpass("Enter the password -> ")
        if name in pas:
            if password == pas.get(name):
                print("\n=============== ")
                print('Name:{}\nAge:{}'.format(
                    (users.get(name).get('name')), (users.get(name).get('age'))))
                print("=============== ")
                wrong = True
            else:
                print("\nWRONG PASSWORD :-[ )")
                again = input("\nTry again(Y/N):")
                if again.lower()[0] == 'y':
                    pass
                else:
                    wrong = True
        else:
            print("\nUNKNOWN USERNAME :-[ ")
            again = input("\nTry again(Y/N):")
            if again.lower()[0] == 'y':
                pass
            else:
                wrong = True


# ADDING NEW USER =====================================================


def check(newPass):
    length = True if 8 <= len(newPass) <= 16 else False
    oneUpper, oneLower, oneSpecial = False, False, False
    for i in newPass:
        if i in string.ascii_lowercase:
            oneLower = True
        elif i in string.ascii_uppercase:
            oneUpper = True
        elif i in string.printable[62:94]:
            oneSpecial = True
    return True if (length and oneLower) and (oneUpper and oneSpecial) else False


def addNew(newName, newPass):
    print("Adding User....")
    pas[newName] = newPass
    users[newName] = {}
    print("ADDED...\nAdd Details Realated to User :-]")
    lastName = input("Last name of the user:")
    age = input("Enter age of user:")
    fullname = '{} {}'.format(newName, lastName)
    users[newName]['name'] = '{}'.format(fullname)
    users[newName]['age'] = age
    print("Details Added for the User:{}".format(newName))
    input()

# Helper Code


def default():
    print('''Criteria for Password:
    1] Must contain a uppercase letter
    2] Must contain a special character
    3] Must contain a digit
    4] Greater than 8 and less than or equal to 16.
    ''')


def clearscreen(command, numlines=100):
    """Clear the console.
  numlines is an optional argument used only as a fall-back.
  """

    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system(command)
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)


# MAIN CODE


if __name__ == '__main__':
    import getpass
    import string
    import os

    pas = {"Vaibhav": "3001Mkgandhi!"}

    users = {'Vaibhav': {'name': 'Vaibhav Singh', 'age': 19},
             }

    userChoice = input("Wish to login or add new or exit (l/a/e):").lower()[0]
    while userChoice != 'e':
        if userChoice == 'l':
            login()
            input()
            clearscreen('clear')

            # print(chr(27) + "[2J")
        elif userChoice == 'a':
            newName = input("Name of the User:")
            nameExist = True if users.get(newName) else False
            while nameExist:
                print("User Exist")
                newName = input('Try new name for the User:')
                nameExist = True if newName in pas.keys() else False
            default()
            newPass = input("Enter Password:")
            test = check(newPass)
            while not test:
                default()
                print("Password Criteria not Satisfied.")
                newPass = input("Enter Password:")
                test = check(newPass)
            addNew(newName, newPass)
            # print(chr(27) + "[2J")
            clearscreen('clear')
        userChoice = input("Wish to login or add new or exit (l/a/e):").lower()[0]
    print("\nProgram Ended")
    input()
    clearscreen("reset")
