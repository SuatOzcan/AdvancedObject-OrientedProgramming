class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        return 'Logged in!'

    def _repr__(self):
        return f'<User {self.username}>'
    
    def __name__(self):
        return f'<User class>'