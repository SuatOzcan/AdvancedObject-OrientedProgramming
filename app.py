from admin import Admin
from database import Database
from user import User

a = Admin('hakan', '1234', 3)
b = User('Asli', '1234')

users = [a,b]

for user in users:
    user.save()

print(Database.find(lambda x : x['username'] == 'hakan'))
print(Database.find(lambda x : x['username'] == 'Asli'))