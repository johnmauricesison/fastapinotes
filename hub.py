
from fastapi import FastAPI
import requests

app = FastAPI()

PROF_URL = "http://localhost:5009"
APPOINT_URL = "http://localhost:5011"


@app.get("/professionals")
def get_professionals():
    prof_response = requests.get(f"{PROF_URL}/professionals")
    return prof_response.json()

@app.get("/professionals/{id}")
def get_professionals_id(id: int):
    prof_response = requests.get(f"{PROF_URL}/professionals/{id}")
    return prof_response.json()

@app.get("/professionals/{id}/appointments")
def get_appointments(id: int):
    appoint_response = requests.get(f"{APPOINT_URL}/professionals/{id}/appointments")
    return appoint_response.json()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5010)
