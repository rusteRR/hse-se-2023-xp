from fastapi import FastAPI

app = FastAPI()

@app.get("/leaderboard")
async def get_results():
    return {}

@app.get("/login")
async def login():
    return {}

@app.post("/homework")
async def homework():
    return {}
