from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel

app = FastAPI()

SHUB_LINK = "http://localhost:5021"

students = []

class Enroll(BaseModel):
    name: str
    year: str
    course_id: int



@app.get("/courses/{id}")
def get_courseid(id: int):
    course_link = requests.get(f"{SHUB_LINK}/courses/{id}")
    return course_link.json()

@app.get("/courses/{id}/students")
def get_students(id: int):
    course_link = get_courseid(id)

    if not course_link:
        raise HTTPException(status_code=404, detail="Course not Found")
    
    record = [a for a in students if a["course_id"] == id]
    return {"Courses": course_link, "Students": record}

@app.post("/courses/{id}/students")
def add_students(id: int, enroll: Enroll):
    course_link = get_courseid(id)
    if not course_link:
        raise HTTPException(status_code=404, detail="Course not Found")
    record = [a for a in students if a["course_id"] == id]

    if len(record) >= course_link["slots"]:
        raise HTTPException(status_code=404, detail="No more slots")
    
    final_students = enroll.dict()
    students.append(final_students)

    return {"Courses": course_link, "Students": final_students}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5022)
    