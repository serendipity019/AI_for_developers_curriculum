from fastapi import FastAPI
from enum import Enum

app = FastAPI(
    title="Enum path parameter",
    version="1.0.1"
)

class Role(str, Enum):
    """
    Enum representing the only valid user roles accepted by the endpoint.
     
    Why inherit from both `str` and `Enum`:
    - `Enum` gives as a fixed set of allowed values.
    - `str` makes enum members behave like strings in amny contexts.

    Allowed values:
    - admin
    - editor
    - viewer 
    """
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"
    
@app.get("/users/{role}")
def list_users(role: Role):
    return {
        "role": role,
        "message" : f"Listing all {role.value}s"
    }
