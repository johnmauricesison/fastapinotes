import fastapi
import requests

app = fastapi.FastAPI()

CATALOG_SERVICE_URL = "http://localhost:5000"

@app.get("/check-availability")
def check_availability(book_id: str):
    try:
        catalog_response = requests.get(f"{CATALOG_SERVICE_URL}/books/{book_id}")
        json = catalog_response.json()
    except:
        return False
    return json["available"]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5002)