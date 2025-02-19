from fastapi import FastAPI
import requests

app = FastAPI()
COURSE_LINK = "http://localhost:5020"

@app.get("/courses")
def get_courses():
    course_link = requests.get(f"{COURSE_LINK}/courses")
    return course_link.json()

@app.get("/courses/{id}")
def get_courseid(id: int):
    course_link = requests.get(f"{COURSE_LINK}/courses/{id}")
    return course_link.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5021)

