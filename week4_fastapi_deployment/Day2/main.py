from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id: int = 0
    title: str
    description: str
    completed: bool

todo_db = []


@app.get("/root")
def root():
    return {"message": "Welcome to the Todo API!"}


@app.get("/status")
def status():
    return {"status": "API is running..."}


@app.post("/todos/")
async def create_todo(todo: Todo):
    todo.id = len(todo_db) + 1
    todo_db.append(todo)
    return todo


@app.get("/todos/")
async def get_todos():
    return todo_db


@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todo_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Item Not Found")


@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todo_db):
        if todo.id == todo_id:
            updated_todo.id = todo_id
            todo_db[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Item Not Found")


@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_db):
        if todo.id == todo_id:
            del todo_db[index]
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Item Not Found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)