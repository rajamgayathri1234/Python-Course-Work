import logic as lg

if lg.login():
    while True:
        lg.menu()
        ch = input("Enter the choice: ").upper()
        if ch == 'C':
            lg.checkbalance()
        elif ch == 'D':
            lg.deposite()
        elif ch == 'W':
            lg.withdraw()
        elif ch == 'V':
            lg.viewtransaction()
        elif ch == 'E':
            print("------------------Thankyou, Visit again------------")
            break
        else:
            print("Enter the valid Choice")                