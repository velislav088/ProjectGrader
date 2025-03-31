from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Project Grader API", version="1.0")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Project Grader API is running!"}
