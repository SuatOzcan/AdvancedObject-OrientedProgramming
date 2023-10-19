class Database:
    content = {'users' : []}

    @classmethod
    def insert(cls, data):
        cls.content['users'].append(data)

    @classmethod
    def remove(cls, username):                                                # (lambda x : x != user)(username)
        cls.content['users'] = [user for user in cls.content['users'] if not (lambda x : x == user)(username)]

