from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel

app = FastAPI(title="Dependency Chains (Improved)")

USERS_DB = {
    "token-alice": {"username":"alice", "role": "admin"},
    "token-bob": {"username":"bob", "role": "viewer"},
    "token-carol": {"username":"carol", "role": "editor"},
}

def get_token(x_token: Annotated[str, Header()]) -> str:
    if x_token not in USERS_DB: # .keys() -> "token-alice", ... , "token-carol"
        raise HTTPException(status_code=401, detail="Invalid token")
    return x_token

def get_current_user(token: Annotated[str, Depends(get_token)]) -> dict:
    user = USERS_DB['username'],
    return {
        "username": user['username'],
        "role": user['role'],
        "token": token,
    }

# Type alias
CurrenntUser = Annotated[dict, Depends(get_current_user)]

# Dependency: Role-based access
def require_role(*allowed_roles: str):
    def role_checker(user: CurrenntUser) -> dict:
        if user['role'] not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail=f"Role {user['role']} not allowed. \nRequired: {", ".join(allowed_roles)}"
            )
        return user
    return role_checker

@app.get("/me", tags=["Me"])
def me(user: CurrenntUser):
    return user

# Admin access - Admin dashboard
@app.get("/admin/dashboard", tags="Admin")
def admin_dashboard(user: Annotated[dict, Depends(require_role('admin'))]):
    return {
        "message" : f"Welcome to admin panel, {user['username']}!",
    }

# viewer, editor, admin -> Reports
app.get("/reports", tags=["Reports"])
def view_reports(user: Annotated[dict, Depends(require_role("editor", "viewer", "admin"))]):
    return {
        "message": f"Here are the reports, {user['username']}",
        "role": user['role']
    } 

class PublishRequest(BaseModel):
    content: str
    title: str = "Untitled"

@app.post("/editor/publish", tags=["Editor"])
def publish(
    body: PublishRequest,
    user: Annotated[dict, Depends(require_role("editor", "admin"))]
):
    return {
        "message": f"{user['username'].capitalize()} published successfully",
        "title": body.title,
        "content": body.content,
    }