from pydantic import BaseModel
from datetime import date
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None  # optional
    status: Optional[str] = "To Do"  # default to "To Do"
    due_date: Optional[date] = None  # optional

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    pass  # inherited from TaskBase


class TaskUpdate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    created_at: date

    class Config:
        orm_mode = True
