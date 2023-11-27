import database.repository as repository

class HomeworkService:
    def get_results(self):
        res = {}
        for result in repository.Repository.get_hw_results():
            hw = repository.Repository.get_result_by_id(result)
            res[result] = res.get(result, []) + [(hw.hw_id, hw.hw_result)]
        return res
    
    def eval_homework(self, hw_id: int, mark: float, comment: str = ""):
        hw = repository.Repository.get_hw_by_id(hw_id)
        hw.set_result(mark)
        hw.set_comment(comment)
