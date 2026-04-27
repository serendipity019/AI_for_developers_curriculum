from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Body + Path + Query", version="1.0.1")

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.put("/items/{item_id}")
def update_item(
    item_id: int,    # Path parameter
    item: Item,      # JSON Body (Pydantic model)
    notify: bool = False # Query parameter
):
    return {
        "item_id": item_id,
        "item": item,
        "notify": notify
    }