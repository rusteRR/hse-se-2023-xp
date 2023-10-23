


class Repository:
    def __init__(self, user_db, homework_db):
        self.user_db     = user_db
        self.homework_db = homework_db

    def get_user_by_id(self, id):
        return self.user_db[id]
    
    def insert_user(self, user):
        self.user_db[user.id] = user
    
    