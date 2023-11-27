class User:
    def __init__(self, id: int, fname: str, sname: str, login: str, password: str, role: str) -> None:
        self.id       = id
        self.fname    = fname
        self.sname    = sname 
        self.login    = login
        self.password = password
        self.role     = role