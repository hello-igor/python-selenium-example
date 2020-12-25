class User:

    def __init__(self):
        self.login = None
        self.password = None
        self.name = None
        self.surname = None

    def set_login(self, login):
        self.login = login

    def set_password(self, password):
        self.password = password
    
    def set_name(self, name):
        self.name = name
    
    def set_surname(self, surname):
        self.surname = surname


class StudentBuilder:

    def __init__(self):
        self.User = User()

    def build(self):
        self.User.set_login('student')
        self.User.set_password('sandbox')
        self.User.set_name('John')
        self.User.set_surname('Smith')
        return self.User


class AdminBuilder:

    def __init__(self):
        self.User = User()
    
    def build(self):
        self.User.set_login('admin')
        self.User.set_password('sandbox')
        return self.User


class InvalidUserBuilder:

    def __init__(self):
        self.User = User()

    def build (self):
        self.User.set_login('user')
        self.User.set_password('12345')
        return self.User