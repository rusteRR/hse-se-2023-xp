import database.repository as repository
import entity.user as user
import database.db as db

class UserService:
    def register_user(self, fname, sname, login, password, role):
        repository.Repository.insert_user(user.User(db.user_id, fname, sname, login, password, role))
        db.user_id += 1
    
    def login_user(self, login, password):
        return repository.Repository.are_correct_credentials()
