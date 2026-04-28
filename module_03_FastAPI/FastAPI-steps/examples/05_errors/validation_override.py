from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI(title="Validation Override", version="1.0.1")

@app.exception_handler(RequestValidationError)
async def validation_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "invalid_request",
            "issues": [
                {
                    "field": ".".join(map(str, e["loc"][1:])),
                    "msg": e['msg']
                }
                for e in exc.errors()
            ],
        },
    )

# e["loc"] = ("path", "item_id")
#            source    parameter name

# map(str, ("items", 0, "name")) -> ["items", 0, "name"]
# ".".join(["items", 0, "name"]) -> "items.0.name"

@app.get("/items/{item_id}", tags=["Items"])
def get_item(item_id: int):
    return {
        "item_id": item_id
    }