#constructor is a special methon . we need not to call the constructor , it's automatically called the parameter.
class Instagram():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(f'Welcome to instagram {self.username}')

gayathri = Instagram('gayathri','123456789')
prasanna = Instagram('prasanna','123456789')

