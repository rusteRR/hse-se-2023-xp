from database.db import users
from database.db import hw
from entity.homework import Homework


class Repository:
    def get_user_by_id(self, id: int):
        return users[id]
    
    def insert_user(self, user: str):
        users[user.id] = user

    def get_hw_results(self):
        return hw.keys()
    
    def get_hw_by_id(self, id: int) -> Homework:
        return hw[id]
    
    def set_filename_to_hw(self, id: int, filename: str):
        hw[id].filename = filename
    
    def are_correct_credentials(self, login: str, password: str):
        for user in users:
            if user.login == login and user.password == password:
                return True
        return False
