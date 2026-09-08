data = {
  123456:{'name':'gayathri','pin':1234,'balance':50000,'history':[]},
  234567:{'name':'prasanna','pin':1234,'balance':80000,'history':[]},
  345678:{'name':'priyanka','pin':1234,'balance':60000,'history':[]},
  456789:{'name':'kalyani','pin':1234,'balance':230000,'history':[]}
 }

def login():
    global acc_num
    acc_num = int(input("Enter the account number: "))
    pin = int(input("Enter tthe pin: "))
    if acc_num in data and data[acc_num]['pin'] == pin:
        print("Login Successfull")
        return True
    else:
       print("Invalid Login")

def menu():
   print(f"Welcome to the ATM, {data[acc_num]['name']}")
   print('[C]hecking Balance')
   print('[D]eposite')
   print('[W]ithdraw')
   print('[V]iew transaction')
   print('[E]xit')

def checkbalance():
    print(f"Hello {data[acc_num]["name"]},")
    print("Current Balance:",data[acc_num]["balance"],end='\n\n')

def deposite():
    amount = int(input("Enter the amount of deposite: "))
    data[acc_num]["balance"] += amount
    data[acc_num]["history"].append(f'{amount} is deposited')
    print(f"{amount} is deposited Successfully")
    checkbalance()

def withdraw():
    amount = int(input("Enter the amount to withdraw:"))
    if data[acc_num]["balance"] >= amount:
        data[acc_num]["balance"] -=amount 
        data[acc_num]["history"].append(f"{amount} is withdraw")
        print(f"{amount} is withdraw Successfully")
        checkbalance()
    else:
        print("Insufficient Balance")

def viewtransaction():
    if data[acc_num]["history"]:
        print("=========== Transaction History ============")
        for i in data[acc_num]["history"]:
            print(i)
        else:
            print("=========End of The History==========")
    else:
        print("No Transaction History")

                    

