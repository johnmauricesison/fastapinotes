
from fastapi import FastAPI

app = FastAPI()

professionals = {
    1:{"id": 1, "name": "Dr. Sison", "max-appointment": 2},
    2:{"id": 2, "name": "Dr. Jann", "max-appointment": 5}
}


@app.get("/professionals")
def get_professionals():
    return list(professionals.values())

@app.get("/professionals/{id}")
def get_professionals_id(id: int):
    return professionals.get(id, {"Error", "Invalid ID"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5009)
