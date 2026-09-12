#self.variable public variable
#self._ protected variable
#self.__private variable
'''
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []

    def getpassword(self):
        return self.__password

    @property
    def accesspost(self):
        return self._post

gayathri = Instagram('gayathri','123456789')

print(gayathri.username)
print(gayathri.getpassword())
print(gayathri.accesspost)
'''
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword

    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        return self._post.append(newpost)

gayathri = Instagram('gayathri','123456789')

print(gayathri.username)
print(gayathri.getpassword())
print(gayathri.accesspost)

gayathri.username = 'gayathri_123'
print(gayathri.username)

gayathri.setpassword ('gayathri@123')
print(gayathri.getpassword())

gayathri.accesspost = 'python intro'
gayathri.accesspost = 'strings'
gayathri.accesspost = 'project'
print(gayathri.accesspost)