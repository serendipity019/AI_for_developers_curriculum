from typing import Annotated
from fastapi import Query, FastAPI

app = FastAPI(
    title= "Query parameters",
    Version="1.0.1"
)

fake_items = [{"name": f"Item-{i}"} for i in range(100)]

@app.get("/items", tags=["Items"])
def list_items(skip: int = 0, limit: int = 10):
    """
    Return a slice of the fake items list.
 
    Key idea:
    Any function parameter that is not part of the path is interpreted
    by FastAPI as a query parameter.
 
    Here:
    - `skip` defaults to 0
    - `limit` defaults to 10
 
    Because both have default values, they are optional.
 
    Example requests:\n
        /items
        /items?limit=5
        /items?skip=20&limit=5
 
    FastAPI also converts query string values automatically:\n
        ?skip=20   -> int
        ?limit=5   -> int
    """
    return {
        "skip": skip,
        "limit": limit,
        "count": len(fake_items[skip: (skip + limit)]),
        "items": fake_items[skip: (skip + limit)]
    }

@app.get("/search", tags=["Search"])
def search(
    q: Annotated[
        str | None,
        Query(
            min_length=3,
            max_length=50,
            description="Search query string",
            examples=["fastapi"]
        )] = None,
    category: Annotated[
        str,
        Query(
            description="Category search in. Defaults to `all`",
            example=["books"]
        )
    ] = "all",
    in_stock: Annotated[
        bool,
        Query(
            description="Whether to return only in-stock items",
            examples=[True]
        )] = False
):
    return {
        "q": q,
        "category": category,
        "in_stock": in_stock 
    }