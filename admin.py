from user import User

class Admin(User):
    def __init__(self, username, password, access):
        super(Admin, self).__init__(username, password)
        self.accesss = access
    
    def __repr__(self):
        return f'<Admin {self.username}, access {self.access}.'
    
    def to_dict(self):
        return {
            'username' : self.user,
            'password' : self.password,
            'access' : self.accesss
        }
    
    def super_usage_with_pretty_algorithm(self):
        return super().pretty_algorithm()
    

adminim =Admin('hakan', 1234,'yes')
variable = adminim.super_usage_with_pretty_algorithm()
print(variable)
print('---------------')
my_name = adminim.username
print(my_name)