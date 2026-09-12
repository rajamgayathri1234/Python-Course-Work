from abc import ABC, abstractclassmethod

class Payment(ABC):
    def source(self):
        print("Scaner/upiid/mobile number")
    def amount(self):
        print("Enter the amount:")
    def bank(self):
        print("Select the bank")
    def pin(self):
        print("Enter the pin")

    @abstractclassmethod
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("Payment success/fail")

class HDFC(Payment):
    def paymentprocess(self):
        print("Payment process through the HBFC bank")

class ICIC(Payment):
    def paymentprocess(self):
        print("Payment process through the ICIC bank")

class UNION(Payment):
    def paymentprocess(self):
        print("Payment process through the UNION bank")

class AXIS(Payment):
    def paymentprocess(self):
        print("Payment process through the AXIS bank")

a = HDFC()
a.source()
a.amount()
a.bank()
a.pin()
a.paymentprocess()
a.paymentstatus()

b = ICIC()
b.source()
b.amount()
b.bank()
b.pin()
b.paymentprocess()
b.paymentstatus()

c = UNION()
c.source()
c.amount()
c.bank()
c.pin()
c.paymentprocess()
c.paymentstatus()

d= AXIS()
d.source()
d.amount()
d.bank()
d.pin()
d.paymentprocess()
d.paymentstatus()