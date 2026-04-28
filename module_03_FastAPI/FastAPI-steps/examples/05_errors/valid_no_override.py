from fastapi import FastAPI

app = FastAPI(title="Valid", version="1.0.1")

@app.get("/users/{user_id}", tags=["Users"])
def get_user(user_id: int):
    return f"User #{user_id}"