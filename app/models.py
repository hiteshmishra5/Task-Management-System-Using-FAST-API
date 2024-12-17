from sqlalchemy import Column, Integer, String, Date
from app.database import Base
import datetime

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, default="To Do")
    due_date = Column(Date, nullable=True)
    created_at = Column(Date, default=datetime.date.today)
