

from fastapi import FastAPI
import requests

app = FastAPI()

PRODUCTS_LINK = "http://localhost:5030"

@app.get("/products")
def get_products():
    products = requests.get(f"{PRODUCTS_LINK}/products")
    return products.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5031)
