from database.repository import Repository
from entity.user import User
from database.db import users
from database.db import user_id


class UserService:
    def register_user(self, fname: str, sname: str, login: str, password: str, role: str):
        Repository.insert_user(User(user_id, fname, sname, login, password, role))
        user_id += 1
    
    def login_user(self, login: str, password: str):
        return Repository.are_correct_credentials()
