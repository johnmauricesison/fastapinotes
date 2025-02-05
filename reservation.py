import fastapi
from pydantic import BaseModel
import uuid
import requests

app = fastapi.FastAPI()
ORCHESTRATOR_SERVICE_URL = "http://localhost:5003"

class Reservation(BaseModel):
    user:str
    book_id:str


reservations = [
    {
        "id" : "1",
        "user": "Sison",
        "book_id": "ISB12"
    }
]

@app.get("/reservations")
def get_reservation():
    return reservations

@app.post("/reservations")
def add_reservation(reservation: Reservation):
    catalog_response = requests.get(f"{ORCHESTRATOR_SERVICE_URL}/check-availability?book_id={reservation.book_id}")
    available = catalog_response.json()
    if available:
        id = str(uuid.uuid4())
        reservations.append({"id" : id, "user" : reservation.user, "book_id" : reservation.book_id})
        return reservation
    else:
        raise Exception("Book not avialable!")
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5004)