#!usr/bin/python3

# USER LOGIN PART =====================================================


def login():
    print("Welcome!!!!")
    wrong = False
    while not wrong:
        name = input("Enter Your First Name:").lower()
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
    return True if length and oneLower and oneUpper and oneSpecial else False


def addNew(newName, newPass):
    print("Adding User....")
    pas[newName] = newPass
    users[newName] = {}
    print("ADDED...\nAdd Details Realated to User :-]")
    lastName = input("Last name of the user:")
    age = input("Enter age of user:")
    users[newName]['name'] = '{} {}'.format(newName, lastName)
    users[newName]['age'] = age
    print("Details Added for the User:{}".format(newName))


def default():
    print('''Criteria for Password:
    1] Must contain a uppercase letter
    2] Must contain a special character
    3] Must contain a digit
    4] Greater than 8 and less than or equal to 16.
    ''')


if __name__ == '__main__':
    import getpass
    import string

    pas = {'vaibhav': 'Infiltrator!@#',
           'rohit': 'COW!@#',
           }

    users = {'vaibhav': {'name': 'Vaibhav Singh', 'age': 19},
             'rohit': {'name': 'Rohit Singh', 'age': 25},
             }

    userChoice = input("Wish to login or add new or exit (l/a/e):").lower()[0]
    while userChoice != 'e':
        if userChoice == 'l':
            login()
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
                newPass = input("Enter Password:")
                test = check(newPass)
            addNew(newName, newPass)
        userChoice = input("Wish to login or add new or exit (l/a/e):").lower()[0]
    print("\nProgram Ended")
