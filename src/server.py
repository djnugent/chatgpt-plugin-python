from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import time

# Create FastAPI application
app = FastAPI()

# Add CORS middleware to accept requests from chat.openai.com
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chat.openai.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static directories to serve static files
app.mount("/plugin", StaticFiles(directory="public/plugin"), name="plugin")
app.mount("/.well-known", StaticFiles(directory="public/.well-known"), name=".well-known")

# Create GET /api/time endpoint
@app.get("/api/time")
async def get_time():
    current_time = datetime.now()
    return {
        "currentTime": current_time.strftime("%H:%M:%S"),
        "currentDate": current_time.strftime("%Y-%m-%d"),
        "currentTimezone": time.strftime("%Z"),
    }