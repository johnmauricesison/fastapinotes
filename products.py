
from fastapi import FastAPI

app = FastAPI()

products = {
    1:{"productId": 1, "name": "T-shirt", "price": 100, "qty": 5},
    2:{"productId": 2, "name": "Shorts", "price": 150, "qty": 2}
}

@app.get("/products")
def get_products():
    return list(products.values())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5030)
