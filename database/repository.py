import database.db as db
from entity.homework import Homework


class Repository:
    def get_user_by_id(self, id: int):
        return db.user_db[id]
    
    def insert_user(self, user: str):
        db.user_db[user.id] = user

    def get_hw_results(self):
        return db.hw.keys()
    
    def get_hw_by_id(self, id: int) -> Homework:
        return db.hw[id]
    
    def are_correct_credentials(self, login: str, password: str):
        for user in db.users:
            if user.login == login and user.password == password:
                return True
        return False
