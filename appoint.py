
from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel

app = FastAPI()

HUB_URL = "http://localhost:5010"

class Appointment(BaseModel):
    appointee_name: str
    contact_number: str
    professional_id: int

appointments = []

@app.get("/professionals")
def get_professionals():
    prof_response = requests.get(f"{HUB_URL}/professionals")
    return prof_response.json()

@app.get("/professionals/{id}")
def get_professionals_id(id: int):
    prof_response = requests.get(f"{HUB_URL}/professionals/{id}")
    return prof_response.json()

@app.get("/professionals/{id}/appointments")
def get_appointments(id: int):
    professionals = get_professionals_id(id)

    if not professionals:
        raise HTTPException(status_code=404, detail="Professional Not Found")
    current_appointment = [a for a in appointments if a["professional_id"] == id]
    return {"professionals" : professionals, "appointments": current_appointment}


@app.post("/professionals/{id}/appointments")
def add_appointments(id: int, appointment: Appointment):
    professionals = get_professionals_id(id)

    if not professionals:
        raise HTTPException(status_code=404, detail="Professionals Not Found")
    current_appointments = [a for a in appointments if a["professional_id"] == id]

    if len(current_appointments) >= professionals["max-appointment"]:
        raise HTTPException(status_code=404, detail="Appointments already full")
    
    new_appointment = appointment.dict()
    appointments.append(new_appointment)

    return {"message": "appointment added", "Appointments": new_appointment}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5011)


    


