from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
import os
import uuid
from datetime import datetime
import logging

# === Setup logging ===
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# === Load environment variables ===
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    logging.error("❌ OPENAI_API_KEY not found in environment.")
    raise RuntimeError("OPENAI_API_KEY not found in environment.")

# === Initialize OpenAI client ===
openai_client = OpenAI(api_key=api_key)

# === FastAPI App Setup ===
app = FastAPI()

# === Middleware ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust to your domains for production security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Mount Static and Templates ===
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# === Summary Directory Setup ===
SUMMARY_DIR = "summaries"
os.makedirs(SUMMARY_DIR, exist_ok=True)

# === Models ===
class TextInput(BaseModel):
    text: str

# === Routes ===

@app.get("/", response_class=HTMLResponse)
def read_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/summarizer", response_class=HTMLResponse)
def summarizer_page(request: Request):
    return templates.TemplateResponse("summarizer.html", {"request": request})

@app.post("/summarize")
async def summarize(input: TextInput):
    try:
        trimmed_text = input.text.strip()
        if not trimmed_text:
            logging.warning("Empty text received for summarization.")
            return JSONResponse(status_code=400, content={"error": "Input text is empty."})

        logging.info("Received text for summarization (truncated): %s", trimmed_text[:100])

        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional summarizer. Return clean, clear summaries without prefacing or disclaimers.",
                },
                {"role": "user", "content": trimmed_text},
            ],
            temperature=0.5,
            max_tokens=300,
        )

        summary = response.choices[0].message.content.strip()
        logging.info("Summary generated successfully.")

        # Save summary to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"summary_{timestamp}_{uuid.uuid4().hex[:6]}.txt"
        filepath = os.path.join(SUMMARY_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(summary)
        logging.info(f"Summary saved to {filepath}")

        return {"summary": summary, "filename": filename}

    except Exception as e:
        logging.error(f"Error during summarization: {e}", exc_info=True)
        return JSONResponse(status_code=500, content={"error": "Internal server error."})

@app.get("/download/{filename}")
async def download_summary(filename: str):
    filepath = os.path.join(SUMMARY_DIR, filename)
    if not os.path.isfile(filepath):
        logging.warning(f"Summary file not found: {filename}")
        return JSONResponse(status_code=404, content={"error": "Summary file not found."})
    return FileResponse(
        filepath,
        media_type="text/plain",
        filename=filename
    )

# === Placeholder Routes for other tools ===

@app.get("/bills", response_class=HTMLResponse)
def bills_placeholder(request: Request):
    return templates.TemplateResponse("placeholder.html", {"request": request, "tool": "Bills Sheet"})

@app.get("/weather", response_class=HTMLResponse)
def weather_placeholder(request: Request):
    return templates.TemplateResponse("placeholder.html", {"request": request, "tool": "Weather Tool"})

@app.get("/monster", response_class=HTMLResponse)
def monster_placeholder(request: Request):
    return templates.TemplateResponse("placeholder.html", {"request": request, "tool": "Monster Generator"})
