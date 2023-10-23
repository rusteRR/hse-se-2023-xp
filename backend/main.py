from fastapi import FastAPI
import service.homework_service as hw_service
import service.user_service as user_service
from models.user_model import User

app = FastAPI()

@app.get("/leaderboard")
async def get_results():
    return hw_service.HomeworkService.get_results()

@app.get("/login")
async def login():
    return {}

@app.post("/register")
async def register(user):
    user_service.UserService.register_user(user.fname, user.sname, user.login, user.password, user.role)

@app.post("/upload")
async def homework():
    return {}

@app.get("/homework/{hw_id}")
async def get_hw(hw: int):
    return {}

@app.post("/eval/homework/{hw_id}")
async def eval_hw(hw: int):
    return {}