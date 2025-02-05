import fastapi
import requests

app = fastapi.FastAPI()

inventory = {
    1:{
        "product-name":"milk",
        "price":"1000 PHP",
        "quantity": "100 pcs"
    },
    2:{
        "product-name":"butter",
        "price":"700 PHP",
        "quantity": "50 pcs"
    }
}

@app.get("/inventory")
def get_inventory():
    return [{"id": id, **b}for id, b in inventory.items()]

@app.get("/inventory/{item_id}")
def get_inventory(item_id: int):
    return inventory[item_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5005)

