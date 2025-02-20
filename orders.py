

from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel

app = FastAPI()
HUB_LINK = "http://localhost:5031"

orders = []

class Order(BaseModel):
    productId : int
    qty: int

@app.get("/products")
def get_products():
    products = requests.get(f"{HUB_LINK}/products")
    return products.json()

@app.get("/orders")
def get_orders():
    prod = get_products()
    om = []

    for a in orders:
        for b in prod:
            if b["productId"] == a["productId"]:
                if b["qty"] > b["qty"]:
                    raise HTTPException(status_code=400, detail="Stock is full")
                
                om.append({
                    "Product": b,
                    "qty": a["qty"],
                    "total": a["qty"] * b["price"]
                })
    return {"Orders": om}
                

@app.post("/orders")
def add_orders(order: Order):
    products = get_products()

    for a in products:
        if a["productId"] == order.productId:
            if order.qty > a["qty"]:
                raise HTTPException(status_code=400, detail="Full Stock")
            
            a["qty"] -= order.qty
            final = order.dict()
            orders.append(final)
            return {"Orders": final}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5032)

