import asyncio
import time
from fastapi import FastAPI

app = FastAPI(title="Sync vs Async")

@app.get("/sync", tags=["Sync"])
def sync_endpoint():
    time.sleep(1)
    return {
        "style": "sync",
        "note": "Ran in a threadpool"
    }

@app.get("/async", tags=["Async"])
async def async_endpoint():
    await asyncio.sleep(1)
    return {
        "style": "async",
        "note": "Ran on event loop"
    } 