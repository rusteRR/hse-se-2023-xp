from fastapi import FastAPI
from service.homework_service import HomeworkService
from service.user_service import UserService
from models.user_model import User
from models.eval_model import Eval

app = FastAPI()

@app.get("/leaderboard")
async def get_results():
    return HomeworkService.get_results()

@app.get("/login")
async def login():
    return {}

@app.post("/register")
async def register(user: User):
    UserService.register_user(user.fname, user.sname, user.login, user.password, user.role)

@app.post("/upload")
async def homework():
    return {}

@app.get("/homework/{hw_id}")
async def get_hw(hw: int):
    return {}

@app.post("/eval/homework")
async def eval_hw(eval: Eval):
    return HomeworkService.eval_homework(eval.hw_id, eval.mark, eval.comment)