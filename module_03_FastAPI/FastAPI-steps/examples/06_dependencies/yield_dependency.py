import time
from typing import Annotated
from fastapi import FastAPI, Depends

app = FastAPI(title="Yield Dependencies")

class FakeDatabase:
    def __init__(self):
        print("[DB] Openning connection")
        time.sleep(1) # simulate slow connection setup
        print("[DB] Connection opened")

    def query(self, sql: str):
        print(f"[DB] Running query: {sql}")
        time.sleep(1)
        print(f"[DB] query complete")
        return f"Return of: {sql}"
    
    def close(self):
        print(f"[DB] Closing connection")
        time.sleep(1) 
        print("[DB] Connection closed")

def get_db():
    print("\n" + "="*50)
    print("Step 1: SETUP — creating the resource")
    print("="*50)
    db = FakeDatabase()   # setup: open connection / create resource
    try:
        print("\nStep 2: YIELD — handing resource to the endpoint")
        print("-"*50)
        yield db          # execution pauses here and the db is passed to the endpoint
    finally:
        print("\nStep 3: TEARDOWN — cleaning up the resource")
        print("-"*50)
        db.close()         # teardown: always runs, even if an error occurs
        print("="*50 + "\n")

@app.get("/data", tags=["Data"])
def read_data(db: Annotated[FakeDatabase, Depends(get_db)]):
    print("  [ENDPOINT] 👉 Using the db inside the endpoint...")
    result = db.query("SELECT * FROM items")
    print("  [ENDPOINT] 👉 Sending response to client...")
    time.sleep(0.5)
    return {"result": result}