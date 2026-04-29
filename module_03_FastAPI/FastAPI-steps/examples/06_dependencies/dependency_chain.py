from typing import Annotated
from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI(title="Dependency Chains")

# Dependency 1: verify token
def get_token(x_token: Annotated[str, Header()]) -> str:
    if x_token != "secret":
        raise HTTPException(401, "Invalid token")
    return x_token

# Dependency 2: depends to Dep.1
def get_current_user(token: Annotated[str, Depends(get_token)]) -> dict:
    return {
        "username": "Alice",
        "token" : token
    }

CurrentUser = Annotated[dict, Depends(get_current_user)]

@app.get("/me", tags=["User"])
def me(user: CurrentUser):
    """
    FastAPI resolves the full dependency chain.
    get_token -> get_current_user -> endpoint
    """
    return user

@app.get("/admin", tags=["Admin"])
def admin(user: CurrentUser):
    return {
        "message": f"Welcome admin {user['username']}"
    }