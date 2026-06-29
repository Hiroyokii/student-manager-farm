from fastapi import FastAPI
from models import Student

app = FastAPI()

students = []
next_id = 1

@app.get("/")
def home():
    return {"Message": "Backend is working!"}

@app.post("/students")
def create_student(student: Student):
    global next_id

    student.id = next_id
    next_id += 1

    students.append(student)
    
    return {
        "message": "Student added successfully",
        "student": student
    }

@app.get("/students")
def get_students():
    return students

@app.delete("/student/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student.id == student_id:

            students.remove(student)

            return {
                "message": "Student deleted!"
            }
        
    return {
        "message": "Student not found."
    }

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    for student in students:

        if student.id == student_id:

            student.name = updated_student.name
            student.age = updated_student.age    
            student.course = updated_student.course

            return {
                "message": "Student updated!",
                "student": student
            }
    
    return {
        "message": "Student not found."
    }
