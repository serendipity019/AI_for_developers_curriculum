from fastapi import FastAPI, HTTPException
from fastapi.responses import (
    HTMLResponse,
    PlainTextResponse,
    RedirectResponse,
    FileResponse,
    StreamingResponse
)
from pydantic import BaseModel
import asyncio
from pathlib import Path


app = FastAPI(title="Custom Response Types")

@app.get("/hello", response_class=PlainTextResponse, tags=["Hello"])
def hello():
    # return "Hello, plain text!"
    return PlainTextResponse("Hello, plain text!")

@app.get("/home", tags=["Home"], response_class=HTMLResponse)
def home():
    html = '''
    <html>
        <head><title>Home</title> </head>
        <body>
            <h1>Welcome to AI for Developers</h1>
            <p>We play with FastAPI</p>
        </body>
    </html>
    '''

    return HTMLResponse(content=html)

@app.get("/greet/{name}", response_class=HTMLResponse, tags=["Greet"])
def greet(name: str, title: str | None = None):
    display = f"{title} {name}" if title else name
    html = f'''
    <html>
        <head><title>Home</title> </head>
        <body>
            <h1>Welcome {display} to AI for Developers</h1>
            <p>We play with FastAPI</p>
        </body>
    </html>
    '''

    return HTMLResponse(content=html)

@app.get("/go")
def go():
    return RedirectResponse("/docs", status_code=307)

@app.get("/download/{filename}", response_class=FileResponse, tags=["Download"])
def download(filename: str):
    save_name = Path(filename).name
    file_path = Path(__file__).parent / save_name
    if not file_path.is_file():
        raise HTTPException(status_code=404, detail=f"File `{save_name}` not found")
    return FileResponse(path=file_path, filename=save_name)

@app.get("/stream", tags=["Stream"])
def stream():
    def generate():
        for i in range(10):
            yield f"Line - {i}\n"
    return StreamingResponse(generate(), media_type="text/plain")

@app.get("/countdown", tags=["Countdown"])
async def countdown():
    async def tick():
        for i in range(10, 0, -1):
            yield f"{i}) ...\n"
            await asyncio.sleep(1)
        yield "BooooooooooooOOOOOMMMM !!!!\n"
    return StreamingResponse(tick(), media_type="text/plain")