from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="Field Validation", version="1.0.1")

class UserCreate(BaseModel):
    username: str = Field(
        ...,           # This mean that is require
        min_length= 3,
        max_length= 20, 
        pattern= r"^[a-z0-9_]+$",
        description="Lowercase letters, numbers and undersore only",
        examples=["John_doe"],
    )
    email: EmailStr = Field(
        ...,
        description="A valid email address",
        examples=["me@gmail.com"],
    )
    age: int = Field(
        ...,
        ge= 18,
        le= 150,
        description="Age must be between 18 and 150",
        examples=[20]
    )
    bio: str | None = Field(
        default= None,
        max_length=500,
        description= "Option short bio with 500 chars max",
        examples= ["Python developer and AI enthusiast"]
    )

@app.post("/users", tags=["Users"])
def create_user(user: UserCreate):
    return {
        "user": user.model_dump(),
        "ok": True
    }