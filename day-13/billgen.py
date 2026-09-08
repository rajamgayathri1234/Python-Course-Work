'''
data = {
    'sugur': 50,
    'rice' : 150,
    'surf powder' : 80,
    'soap' : 40,
    'salt' : 80,
    'milk packets' : 40,
    'cooldrinks' : 70,
    'biscuts' : 60,
    'peanuts' : 49,
    'butter' : 100
}
for i in data:
    print(i.ljust(20),data[i])
prod = input("Enter thr products:").split() 
print("-----------------Bill---------------") 
bill = 0
for i in prod:
    print(i.ljust(20),data[i])
    bill += data[i]
print("Total Bill".ljust(20),bill)    
   '''

data = {
    'sugur': 50,
    'rice' : 150,
    'surf powder' : 80,
    'soap' : 40,
    'salt' : 80,
    'milk packets' : 40,
    'cooldrinks' : 70,
    'biscuts' : 60,
    'peanuts' : 49,
    'butter' : 100
}
for i in data:
    print(i.ljust(20),data[i])
bill = 0
while True:
    product = input("Enter the product name or [E]xit:" )
    if product == 'E' or product == 'e':
        print("Thanks for shopping")
        print("Total bill",bill)
        break
    else:
        quantity = int(input("enter the quantity:"))
        bill += data[product]*quantity