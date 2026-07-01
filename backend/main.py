from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas import StudentCreate
from app.crud import create_student

app = FastAPI()

@app.post("/students")
def add_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return create_student(db, student)

