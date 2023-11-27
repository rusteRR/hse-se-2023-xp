class Result:
    def __init__(self, hw_id: int, mark: float, comment: str = "", fixes: bool = False):
        self.hw_id   = hw_id
        self.mark    = mark
        self.comment = comment
        self.fixes   = fixes