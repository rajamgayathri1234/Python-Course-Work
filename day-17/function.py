'''
def functionname(arg):
    #statements
    return (opt)

functionname(para)    

def gst(price):
    print("Original Price:",price)
    print("Final Price:",price+price*0.18)

gst(1000)
gst(700)
gst(500)
gst(8000)    

def table(n):
    print(f'{n}-Table')
    print('--------------------')
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')

for i in range(1,21):
    table(i)
    
def isleap(year):
    if year % 400 == 0 or ( year%4 == 0 and year%100 != 0):
        return "Leap Year"
    else:
        return"Not a Leap Year"

print(isleap(2000))    
'''
