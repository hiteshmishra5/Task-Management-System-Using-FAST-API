from sqlalchemy.orm import Session
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate

def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, status: str = None, order_by: str = 'created_at'):
    query = db.query(Task)
    if status:
        query = query.filter(Task.status == status)
    if order_by == 'created_at':
        query = query.order_by(Task.created_at)
    elif order_by == 'due_date':
        query = query.order_by(Task.due_date)
    return query.all()

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(db: Session, task_id: int, task_update: TaskUpdate):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        for key, value in task_update.dict(exclude_unset=True).items():
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
    return task



def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task
