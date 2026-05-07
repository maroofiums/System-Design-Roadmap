from fastapi import FastAPI 
from app.core.database import engine, Base 
from app.routes.prediction_routes import router 

Base.metadata.create_all(bind=engine) 

app = FastAPI( title="Production Iris ML API" ) 

app.include_router(router) 

@app.get("/") 
def home(): 
    return { "message": "Production ML API Running" }