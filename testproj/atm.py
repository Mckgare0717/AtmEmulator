import json
import datetime
import os
import sys

with open("userData.json","r") as openFile:

    data = json.load(openFile)

enterAmount = 0
def deposit(i):
    flag = False
    while flag == False:
        try:
            enterAmount = int(input("Enter amount you want to deposit: "))
            data["users"][i]["balance"] += enterAmount
    
            transactions = {}
            transactions["transaction"] = "deposit"
            transactions["dateTime"] = datetime.datetime.now()
            transactions["amount"] = enterAmount
            data["users"][i]["statement"].append(transactions)
            os.system("cls")
            print("your new balance is £",data["users"][i]["balance"])
            flag = True
        except:
            print("Enter a number")
            flag = False
    
    
    

def withdraw(i):
    flag = False
    while flag == False:
        try:
            enterAmount = int(input("Enter amount you want to withdraw: "))
            data["users"][i]["balance"] -= enterAmount
    
            transactions = {}
            transactions["transaction"] = "Withdraw"
            transactions["dateTime"] = datetime.datetime.now()
            transactions["amount"] = enterAmount
            data["users"][i]["statement"].append(transactions)
            os.system("cls")
            print("your new balance is £",data["users"][i]["balance"])
            flag = True
        except:
            print("enter a  number")
            flag = False
    
def login():
    flag = False
    contUser = "y"
    while contUser == "y":
   
    
    
        while flag == False:
            userChoice = 0
            userName = input("enter user name: ")
            psswd = input("Enter psswd: ")
            os.system("cls")
            for i in range(len(data["users"])):
                    if userName == data["users"][i]["userName"] and psswd == data["users"][i]["pin"]:
                        print("\t\twelcome to HSBC bank ATM emulator\t\t")
                        print("name: ",data["users"][i]["userName"])
                        while userChoice != 5:
                            print("1:deposit\n2:withdraw\n3:view balance\n4:view statement\n5:Exit")
                            try:
                                userChoice = int(input("Enter your choice: "))
                            except:
                                os.system("cls")
                                print("enter valid number")
                            if userChoice == 1:
                                deposit(i)
                            elif userChoice == 2:
                                withdraw(i)
                            elif userChoice == 3:
                                os.system("cls")
                                                                                                   
                                print("your balance is: ",data["users"][i]["balance"])
                            elif userChoice == 4:
                                os.system("cls")
                                for j in data["users"][i]["statement"]:
                                    print(j)
                            elif userChoice == 5:
                                try:
                                    sys.exit("thank you for coming ,have an amazing day ahead")
                                except:
                                    print("thank you for coming ,have an amazing day ahead")
                                    #os.system("cls")
                                contUser = input("'y' to continue, 'n'to exit: ")
                                if contUser == "n":
                                    def myconverter(o):
                                        if isinstance(o, datetime.datetime):
                                            return o.__str__()
                                    with open("userData.json","w") as openFile:
                                        json.dump(data,openFile,indent=4,default=myconverter)
                                        openFile.close()
                                    quit()
                                break
                            else:
                                os.system("cls")
                                print("invalid input")
                    
            
        
                    else:
                    
                        flag = False
        

        
    
        




