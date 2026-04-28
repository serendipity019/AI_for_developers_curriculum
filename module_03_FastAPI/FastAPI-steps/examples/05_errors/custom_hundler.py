from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="Custom Exception Handler", version="1.0.1")

# Step 1: Define a custom exception class
class BusinessError(Exception):
    def __init__(self, code: str, msg:str):
       self.code = code
       self.msg = msg

# Step 2: Register a handler for it
# What does it mean to register a handler?
# If anywhere in application a Bussinesses error occurs, then execute this function
@app.exception_handler(BusinessError)
async def bussiness_error_handler(request: Request, exc: BusinessError):
    return JSONResponse(
        status_code=422,
        content={
            "code": exc.code,
            "message": exc.msg
        }
    )

# Step 3: Raise it in our endpoints
@app.post("/orders", tags=["Orders"])
def place_order(n: int):
    if n <= 0:
        raise BusinessError("INVALID QUANTITY", "Quantity must be positive")
    return {
        "ok": True,
        "quantity": n
    }