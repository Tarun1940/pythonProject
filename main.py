from fastapi import FastAPI

app = FastAPI()
@app.get('/')
async def root():
    return{
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": "False"
    }