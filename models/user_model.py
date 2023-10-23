from pydantic import BaseModel

class User(BaseModel):
    fname: str
    sname: str
    login: str
    password: str
    role: str
