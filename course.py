from fastapi import FastAPI

app = FastAPI()

courses = {
    1:{"id":1, "name": "ITELE102", "slots": 2},
    2:{"id":2, "name": "ITELE104", "slots": 2},
    3:{"id":3, "name": "ITELE105", "slots": 2}
}

@app.get("/courses")
def get_courses():
    return list(courses.values())

@app.get("/courses/{id}")
def get_courseid(id: int):
    return courses.get(id, "Course not Found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5020)
