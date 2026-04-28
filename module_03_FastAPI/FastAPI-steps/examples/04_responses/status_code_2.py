from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI(title="Status Codes", version="1.0.1")

class Item(BaseModel):
    name: str = Field(..., description="The name of the item", example=["Bag"])
    price: float = Field(..., description="The price of the item", example=[8.5])

app.state.items_db: dict[int, Item] = {}
app.state.counter = 0

@app.post("/items", tags=["Items"], status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    app.state.items_db[app.state.counter] = item
    app.state.counter += 1
    return item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
def delete_item(item_id: int):
    app.state.items_db.pop(item_id, None)

# TODO: get all the items

# TODO: get item (using item_id)