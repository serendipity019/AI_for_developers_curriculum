from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI(
    title= "Query lists and Booleans",
    version="1.0.1",
    port= 8001
)

@app.get("/products", tags=["Products"])
def products(
    tags: Annotated[list[str] | None, Query()] = None,
    min_price: float =0,
    on_sale: bool = False
):
    """
    - Repeat a query key for lists: ?tags=red&tags=blue
    - Booleans accept: true/false, 1/0, yes/no
    """
    return {"tags": tags, "min_price": min_price, "on_sale": on_sale}
 
@app.get(
    "/products",
    summary="Filter products using query parameters",
    description=(
        "Accepts optional query parameters for tags, minimum price, and "
        "sale status. Repeated query keys are collected into a list."
    ),
    tags=["Products"],
)
def products(
    tags: Annotated[
        list[str] | None,
        Query(
            description="Optional list of product tags. Repeat the query key to provide multiple values.",
            examples=[["red", "blue"]],
        ),
    ] = None,
    min_price: Annotated[
        float,
        Query(
            description="Minimum product price to include in the results.",
            examples=[9.99],
        ),
    ] = 0,
    on_sale: Annotated[
        bool,
        Query(
            description="Filter products based on whether they are on sale.",
            examples=[True],
        ),
    ] = False,
):
    """
    Return the query parameters after FastAPI validation and conversion.
 
    Query parameters used here:
 
    - `tags`
      Repeating the same query key creates a list.
      Example:\n
          ?tags=red&tags=blue
 
    - `min_price`
      FastAPI converts the incoming string to a float automatically.
      Example:\n
          ?min_price=9.99
 
    - `on_sale`
      FastAPI accepts several boolean-like string values and converts them
      to Python bool.
      Common accepted values include:\n
          true / false
          1 / 0
          yes / no
          on / off
 
    Example requests:\n
        /products
        /products?tags=red
        /products?tags=red&tags=blue&min_price=9.99&on_sale=true
        /products?on_sale=yes
    """

    return {
        "tags": tags,
        "min_price": min_price,
        "on_sale": on_sale,
        "types": {
            "tags": type(tags).__name__ if tags is not None else None,
            "min_price": type(min_price).__name__,
            "on_sale": type(on_sale).__name__,
        },
    }