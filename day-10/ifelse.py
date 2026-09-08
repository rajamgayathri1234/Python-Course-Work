'''Username = input("UserName:")
Password = input("Password:")
if Username == 'admin' and Password == "admin123":
    print("Login Successful")
else:
    print("invalid Creditionals")    
  
products = ['bag', 'laptop','charger','pen','bottle']
search = input("enter product:")
if search in products:
    print(f'{search} found')
else:
    print(f'{search} not found')
'''
bill = int(input("enter the bill:"))
if bill > 99:
    print("Total Amount:",bill)
else:
    print("bill + delivery charg: ",bill+30)    
