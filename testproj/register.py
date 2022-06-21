import json
import datetime
import main
data = main.openFileNw()

def userRegister():
    #print("'y':yes\n'n':no")
    userAdd = "y"
    while userAdd == "y":
        register = input("do you want to register\n'y':yes\n'n':no: ")
        if register == "y":
            userName = input("enter your new username: ")
            pin = int(input("enter new Pin: "))
            userBal = input("do you want to add some amount in your account\n'y':yes\n'n':no: ")
            if userBal == "y":
                balance = int(input("Enter amount you want to add to your account: "))
            else:
                balance = 0
            newUser = {}
            newUser["userName"] = userName
            newUser["pin"] = str(pin)
            newUser["balance"] = balance
            newUser["statement"] = []
            transactions = {}
            transactions["transaction"] = "Deposit"
            transactions["dateTime"] = datetime.datetime.now()
            transactions["amount"] = balance
            newUser["statement"].append(transactions)
            data["users"].append(newUser)
            def myconverter(o):
                if isinstance(o, datetime.datetime):
                    return o.__str__()
            with open("userData.json","w") as openFile:
                json.dump(data,openFile,indent=4,default=myconverter)
            print("new user created")
            print("User Name: ",newUser["userName"])
            print("Pin: ",newUser["pin"])
            print("Balance: ",newUser["balance"])
            openFile.close()




        else:
            quit()
        userAdd = input()
openFile.close()

#userRegister()