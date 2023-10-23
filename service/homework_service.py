import database.db as db

class HomeworkService:
    def get_results(self):
        res = {}
        for result in db.results:
            res[result.user_id] = res.get(result.user_id, []) + [(result.hw_id, result.hw_result)]
        return res 