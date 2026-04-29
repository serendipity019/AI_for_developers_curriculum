from pathlib import Path
from fastapi import FastAPI, BackgroundTasks

app = FastAPI(title="Background tasks")

LOG_FILE = Path("background_log.txt")

def write_log(message: str):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")
    print(f" [BG] Logged: {message}")

@app.post("/send-email", tags=["Email"])
def send_email(to: str, bg: BackgroundTasks):
    """
    Background tasks runs fire-and-forget work after response.
    The gets an immediate response. The 'logs' happens later.

    For heavy jobs, use Celery, Dramatiq.
    """
    bg.add_task(write_log, f"Email sent to {to}")
    return {
        "status": "queued",
        "to": to
    }
