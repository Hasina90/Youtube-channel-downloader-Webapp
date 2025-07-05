from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import os


# 1. Create FastAPI app
app = FastAPI()

# 2. Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 3. Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Route for home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 5. Route to handle video downloads
@app.post("/download/")
async def download(channel_url: str = Form(...)):
    if not channel_url:
        return JSONResponse(content={"error": "No URL provided"}, status_code=400)

    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)

    try:
        command = [
            "yt-dlp",
            "--yes-playlist",
            "--format", "mp4",
            "-o", os.path.join(download_dir, "%(title)s.%(ext)s"),
            channel_url
        ]
        subprocess.run(command, check=True)
        return {"message": f"Download completed. Files saved in: {download_dir}"}
    except subprocess.CalledProcessError:
        return JSONResponse(content={"error": "Download failed"}, status_code=500)
@app.post("/stop-download/")
async def stop_download():
    global download_process

    if download_process and download_process.poll() is None:
        download_process.terminate()
        return {"message": "Download stopped."}
    else:
        return {"message": "No active download to stop."}