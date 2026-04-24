from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/about")
async def about():
    return {"about":"My first API"}

@app.get("/name")
async def name():
    return {"name": "Maroof"} 

@app.get("/goal")
async def goal():
    return {"goal": "To become a successful Machine Learning Engineer"}

@app.get("/hobby")
async def hobby():
    return {"hobby": "Playing football and coding"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)