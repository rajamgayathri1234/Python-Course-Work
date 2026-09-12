#create another child class(driver) for red bus and they need to see user info(like which seat user booked) 
# and hide the driver personal details
#and display the driver name and phone number

class Redbus:
    bus = {i: "Available" for i in range(1,11)}

    def displayseats(self):
        print("---------xyz bus----------")
        for i in Redbus.bus:
            print(i,Redbus.bus[i])

    def booking(self,seatno):
        for i in Redbus.bus:
            if i == seatno and Redbus.bus[i] == "Available":
                Redbus.bus[i] =  'Booked'
                print(f'your seat {seatno} is booked successfully!')
                break
        else:
            print(f'seat {seatno} is already booked, choose another seat')

class Driver(Redbus):
    def __init__(self,name,phoneno,age,experience):
        self.name = name
        self.phoneno = phoneno
        self.__age = age
        self.__experience = experience

    def display_driver(self):
        print("------Driver Details-------")
        print("Driver naeme:",self.name)
        print("Driver phone no:",self.phoneno)


        
class User(Redbus):
    def __init__(self,name,email,phoneno):
        self.name = name
        self.email = email
        self.phoneno = phoneno

a = User('gayathri','gayathri@gmail.com','98765432')
b = User('prasanna','prasanna@gmail.com','98765432')
c = User('priyanka','priyanka@gmail.com','65432890')
d = Driver('Suresh','234567890','28','5years')
d.display_driver()
a.displayseats()
a.booking(4)  
b.displayseats()
b.booking(8)  
c.displayseats()
c.booking(1)  
