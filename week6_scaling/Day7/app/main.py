from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Scalable ML API")

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Scalable ML API Running!..."
    }