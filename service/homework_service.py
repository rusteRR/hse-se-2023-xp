from entity.result import Result
from models.hw_model import Hw
from database.repository import Repository

class HomeworkService:
    def get_results(self):
        res = {}
        for result in Repository.get_hw_results():
            hw = Repository.get_result_by_id(result)
            res[result] = res.get(result, []) + [(hw.hw_id, hw.hw_result)]
        return res
    
    def eval_homework(self, hw_id: int, mark: float, comment: str = "", fixes: bool = False):
        Repository.insert_result(Result(hw_id, mark, comment, fixes))
        if fixes:
            Repository.get_hw_by_id(hw_id).change_status()
    
    def upload_homework(self, hw_id: int, filename: str):
        Repository.set_filename_to_hw(hw_id, filename)
