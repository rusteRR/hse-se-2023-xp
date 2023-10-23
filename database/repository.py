import database.db as db


class Repository:
    def get_user_by_id(self, id):
        return db.user_db[id]
    
    def insert_user(self, user):
        db.user_db[user.id] = user

    def get_result(self):
        return db.results.keys()

    def get_result_by_id(self, id):
        return db.results[id]
    
    def are_correct_credentials(self, login, password):
        for user in db.users:
            if user.login == login and user.password == password:
                return True
        return False
