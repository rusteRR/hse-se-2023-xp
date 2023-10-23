
class User:
    def __init__(self, id, fname, sname, login, password, role) -> None:
        self.id       = id
        self.fname    = fname
        self.sname    = sname 
        self.login    = login
        self.password = password
        self.role     = role

class Homework:
    def __init__(self, user_id, hw_id, hw_result):
        self.user_id   = user_id
        self.hw_id     = hw_id
        self.hw_result = hw_result

users   = {}
results = {}