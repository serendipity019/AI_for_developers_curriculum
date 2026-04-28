from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(title="Status Codes", version="1.0.1")

class Item(BaseModel):
    name: str
    price: float

items_db: dict[int, Item] = {}
counter = 0

@app.post("/items", tags=["Items"], status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    global counter
    items_db[counter] = item
    counter += 1
    return item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Delete items"])
def delete_item(item_id: int):
    items_db.pop(item_id, None)
