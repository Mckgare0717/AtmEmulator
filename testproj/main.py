import atm as existingCust
import register as newCust
import os
import tkinter

def __main__():
    print("\t\tWelcome to Hsbc Bank services\t\t")
    userCont = "y"
    while userCont == "y":
        print("1:Register New User\n2:Login Existing User\n3:Exit")
       
        userChoice = int(input())

        if userChoice == 1:
            newCust.userRegister()
        elif userChoice == 2:
            existingCust.login()
        else:
            #quit()
            os.exit()
__main__()

def openFileNw():
    with open("userData.json","r") as openFile:
        openFile.seek(0)
        data = json.load(openFile)
        return data