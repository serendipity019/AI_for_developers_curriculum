from fastapi import FastAPI

app = FastAPI(
    title= "Path parameteres",
    description= "Demonstrates how to validate and handle path parameters",
    version="1.0.0"
)

@app.get("/users/{user_id}",
         summary="Get a user by numeric id.",
         description="Accepts a user id as a path parameter.",
         tags=["Users"])
def get_user(user_id: int):
    """
    Return a user identifier received from the URL path.
    
    The type hint `int` is important because FastAPI uses it to:
    1. Validate that the incoming value is a valid integer.
    2. Convert the path value from string to int automatically.
    3. Reject invalid values before entering the function.
     
    Example:
    /users/42 -> valid
    /users/abc -> invalid, returns 422 """

    return {
        "user_id" : user_id, # Returns the integer user id.
        "kind" : type(user_id).__name__ # shows that the value is really an int
    }

@app.get("/files/{file_path:path}",
         tags={"Files"})
def read_file(file_path: str):
    
    return {"file_path": file_path}