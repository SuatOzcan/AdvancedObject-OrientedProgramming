from admin import Admin
from database import Database
from user import User
from saveable import Saveable

a = Admin('hakan', '1234', 3)

a.save()

print(Database.find(lambda x : x['username'] == 'hakan'))