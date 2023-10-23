class User:
    def __init__(self, id, fname, sname, login, password, role) -> None:
        self.id       = id
        self.fname    = fname
        self.sname    = sname 
        self.login    = login
        self.password = password
        self.role     = role