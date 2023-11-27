class Homework:
    def __init__(self, user_id: int, hw_id: int, hw_result: float, comment: str):
        self.user_id   = user_id
        self.hw_id     = hw_id
        self.hw_result = hw_result
        self.comment   = comment
    
    def set_result(self, hw_result: int):
        self.hw_result = hw_result

    def set_comment(self, comment: str):
        self.comment   = comment