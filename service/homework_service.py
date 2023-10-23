import database.repository as repository

class HomeworkService:
    def get_results(self):
        res = {}
        for result in repository.get_results():
            hw = repository.Repository.get_result_by_id(result)
            res[result] = res.get(result, []) + [(hw.hw_id, hw.hw_result)]
        return res 