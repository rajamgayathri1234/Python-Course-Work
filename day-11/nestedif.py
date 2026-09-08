'''fa = eval(input("Follow Account:"))
if fa:
    cf = eval(input("Close Friend:"))
    if cf:
        print("Visible the story")
    else:
        print("Not in Close friend list")
else:
    print("First Follow Account first")            

reg = eval(input("Registration Status:"))
if reg:
    fees = eval(input("Fee Paid:"))
    if fees:
        print("Entry is Conformed")
    else:
        print("Entry Fee Required:")
else:
    print("Registration Required")   
    

link = eval(input("Link Active:"))
if link:
    perm = eval(input("Permission Granted:"))
    if perm:
        print("File Opended Successfully") 
    else:
        print("Access Denied")
else:
    print("invalid Link")    
    '''

data = {
    'gayathri':{'status':True,'python':89,'mysql':92,'flask':90},
    'prasanna':{'status':True,'python':90,'mysql':89,'flask':97},
    'raju':{'status':False,'python':None,'mysql':None,'flask':None},
    'priyanka':{'status':True,'python':46,'mysql':52,'flask':92},
    'keerthana':{'status':True,'python':34,'mysql':28,'flask':56},
    'anusri':{'status':True,'python':76,'mysql':65,'flask':49}

}
name = input("Enter the name: ") 
if name in data:
    if data[name]['status']:
        sum = data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg = sum/3
        print(f'Hello {name}')
        print(f'Your Average Score is {avg}')
        if avg > 90:
            print("OutStanding Performance")
        elif avg > 80:
            print("Very Good")
        elif avg > 60:
            print("Good , Work Hard")
        else:
            print("You fail the exam, Work Hard")   
    else:
        print(f'{name} did not attend the exam')
else:
    print(f"{name} is not found in the data")
