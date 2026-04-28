from typing import Annotated
from fastapi import Depends, FastAPI

app = FastAPI(title="Class Dependencies")

fake_items = [{"name": f"Item {i}"} for i in range(100)]

class Pager:
    def __init__(self, skip: int = 0, limit: int = 10):
        self.skip = skip
        self.limit = limit

@app.get("/items", tags=["Items"])
def list_items(p: Annotated[Pager, Depends()]):
    return fake_items[p.skip : (p.skip + p.limit)]