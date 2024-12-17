from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from app import models, crud, auth, schemas

from app.schemas import TaskCreate

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Post a tasks
@app.post("/tasks/")
def create_task(task: TaskCreate, db: Session = Depends(get_db), token: str = Depends(auth.get_current_user)):
    return crud.create_task(db, task)


# Get all tasks
@app.get("/tasks/")
def get_tasks(status: str = None, order_by: str = 'created_at', db: Session = Depends(get_db), token: str = Depends(auth.get_current_user)):
    return crud.get_tasks(db, status, order_by)

# Get a task by ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db), token: str = Depends(auth.get_current_user)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update a task
@app.put("/tasks/{task_id}", response_model=schemas.TaskUpdate)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = crud.update_task(db=db, task_id=task_id, task_update=task_update)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), token: str = Depends(auth.get_current_user)):
    task = crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
