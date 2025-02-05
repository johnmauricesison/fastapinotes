import fastapi

app = fastapi.FastAPI()

books = {
    "ISB1234": {
        "name" : "Hello me",
        "available" : True
    },

    "ISB5678": {  # Changed the book_id
        "name" : "Hello hi",
        "available" : True
    }
}


@app.get("/books")
def get_books():
    return [{"id": id, **b} for id, b in books.items()]


@app.get("/books/{book_id}")
def get_book(book_id: str):
    return books[book_id]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)