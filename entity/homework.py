from datetime import datetime

class Homework:
    def __init__(self, user_id: int, hw_id: int, deadline: datetime):
        self.user_id   = user_id
        self.hw_id     = hw_id
        self.deadline  = deadline
        self.is_done   = False 
    
    def change_status(self):
        self.is_done ^= True