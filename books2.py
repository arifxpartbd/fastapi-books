from fastapi import FastAPI

app = FastAPI()

BOOKS = []

@app.get("/")
async def books():
    return BOOKS