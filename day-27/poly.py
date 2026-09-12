#method overriding
class Hotstar:
    def __init__(self,name):
        print(f'Welcome to the hoststar, {name}-------------')
    def auth(self):
        print("You can login/register")
    def dashboard(self):
        print("you can see the dashboard")
    def search(self):
        print("ypu can search")
    def history(self):
        print("you can see the history")
    def playcontroller(self):
        print("Pause play resumes")
    def ads(self):
        print("Ads will be run")
    def quality(self):
        print("You have limited quality")
    def devices(self):
        print("you have a single login")
    def access(self):
        print("Limited access")
    def download(self):
        print("you can't download")                                        

class PremiumHotstar(Hotstar):
    def __init__(self,name):
        print(f'Welcome to the hoststar, {name}-------------')
    def auth(self):
        print("You can login/register")
    def dashboard(self):
        print("you can see the dashboard")
    def search(self):
        print("ypu can search")
    def history(self):
        print("you can see the history")
    def playcontroller(self):
        print("Pause play resumes")
    def ads(self):
        print("no ads wii be run")
    def quality(self):
        print("You have high quality")
    def devices(self):
        print("you have a multiple login")
    def access(self):
        print("access in your permissions")
    def download(self):
        print("you can download") 

a = Hotstar('a')
a.auth()
a.dashboard()                                              
a.search
a.history()
a.playcontroller()
a.ads()
a.quality()
a.devices()
a.access()
a.download()

b = PremiumHotstar('b') 
b.auth()
b.dashboard()                                              
b.search
b.history()
b.playcontroller()
b.ads()
b.quality()
b.devices()
b.access()
b.download()