from fastapi import FastAPI
import service.homework_service as hw_service

app = FastAPI()

@app.get("/leaderboard")
async def get_results():
    return hw_service.HomeworkService.get_results()

@app.get("/login")
async def login():
    return {}

@app.post("/homework")
async def homework():
    return {}
