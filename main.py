tempArray = []
run = True
global loggedIn
loggedIn = "nil"

def Encryption(p):

    tempWord = str(p)
    for x in range(len(p)):
        tempLetter = ord(tempWord[x]) * 543697
        tempArray.append(tempLetter)
    encryptedPass = ""
    for x in range(len(p)):
        encryptedPass = encryptedPass + str(tempArray[x])
    return encryptedPass

def CreateAccount():
    file = open("logins.txt", 'r+')
    validUser = False
    while validUser == False:
        userInput = input("Please enter a username")
        if userInput in file.read():
            print("Username already in use, please pick another user")
        else:
            validUser = True
    userPassword = Encryption(input("Please enter a password"))
    file.writelines(userInput+userPassword+"\n")
    file.close()

def Login():
    file = open("logins.txt" , "r+")
    userName = input("What is your username?")
    userPassword = Encryption(input("What is your password?"))
    userCombo = userName+userPassword
    if userCombo in file.read():
        print("Logged in")
        loggedIn = userName
    else:
        print("Username or Password incorrect")

while run:
    print("Would you like to\n1.Create an account\n2.Login\n3.Check account info")
    userInput = input()
    if userInput == '1':
        CreateAccount()
    elif userInput == '2':
        Login()
    elif userInput == '3':
        print(loggedIn)
