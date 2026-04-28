from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="Respone Model",
    version="1.0.1"
)

class UserIn(BaseModel):
    """What the client sends (include passwords)"""
    username: str
    password: str
    email: EmailStr

class UserOut(BaseModel):
    """What the API returns (without password)"""
    username: str
    email: EmailStr

# In-memory storagy for demo
users_bd: list[dict] = []

@app.post("/users", tags=["Users"], response_model=UserOut)
def create_user(user: UserIn):
    users_bd.append(user)
    return user

