'''
#single inheritance  we can access parent class to child class
class Whatsappv1:
    def message(self):
        print("You can send a message")

class Whatsappv2(Whatsappv1):
    def status(self):
        print("You can upload the status for 24hrs")

gayathri = Whatsappv1()
gayathri.message()

prasanna = Whatsappv2()
prasanna.message()
prasanna.status()

#multilevel 
class Whatsappv1:
    def message(self):
        print("You can send a message")

class Whatsappv2(Whatsappv1):
    def status(self):
        print("You can upload the status for 24hrs")
class Whatsappv3:
    def groupes(self):
        print("you can add the groupes")

gayathri = Whatsappv1()
gayathri.message()

prasanna = Whatsappv2()
prasanna.message()
prasanna.status()

priyanka = Whatsappv3()
priyanka.groupes()


class Whatsappv1:
    def message(self):
        print("You can send a message")

class Whatsappv2(Whatsappv1):
    def status(self):
        print("You can upload the status for 24hrs")
class Whatsappv3:
    def groupes(self):
        print("you can add the groupes")
class Whatsappv4:
    def community(self):
        print("You can combine multiple groupes")

class Whatsappv5(Whatsappv4,Whatsappv3,Whatsappv2):
    def channels(self):
        print("You can post with regular with huge crowd")     


a = Whatsappv5()
a.message()
a.status()
a.groupes()
a.community()
a.channels()


class Whatsappv1:
    def message(self):
        print("You can send a message")

class Whatsappv2(Whatsappv1):
    def status(self):
        print("You can upload the status for 24hrs")
class Whatsappv3(Whatsappv1):
    def groupes(self):
        print("you can add the groupes")
class Whatsappv4(Whatsappv1):
    def community(self):
        print("You can combine multiple groupes")

a = Whatsappv1()
a.message()

b = Whatsappv2()
b.message()
b.status()

c = Whatsappv3()
c.message()
c.groupes()

d = Whatsappv4()
d.message()
d.community()
'''
