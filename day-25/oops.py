class Flipkart:
    discount = 30  

    @classmethod
    def updatediscount(cls):
        cls.discount = 40
        print("Updated Discount:",cls.discount)

    def info(self,name,phoneno,address):
        self.name = name
        self.phoneno = phoneno
        self.address = address
        print(f'Welcome to the flikart',self.name)

    @staticmethod
    def banner():
        print(f"{Flipkart.discount}% discount is going, grab the offer")

gayathri = Flipkart()
gayathri.info('gayathri',987654321,'Hyd')
gayathri.updatediscount()
gayathri.banner()

prasanna = Flipkart()
prasanna.info('prsanna',987654321,'bnglr')
prasanna.updatediscount()
prasanna.banner()

priyanka = Flipkart()
priyanka.info('priyanka',987654321,'ch')
priyanka.updatediscount()
priyanka.banner()