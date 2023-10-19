from admin import Admin
from database import Database

a = Admin('hakan', '1234', 3)

a.save()

print(Database.find(lambda x : x['username'] == 'hakan'))