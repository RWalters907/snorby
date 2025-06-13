from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found in environment.")
openai_client = OpenAI(api_key=api_key)

# Initialize FastAPI app
app = FastAPI()

# CORS (adjust for production if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static and templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# === Homepage ===
@app.get("/", response_class=HTMLResponse)
def read_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# === Summarizer ===
@app.get("/summarizer", response_class=HTMLResponse)
def summarizer_page(request: Request):
    return templates.TemplateResponse("summarizer.html", {"request": request})

@app.post("/summarize")
async def summarize(text: str = Form(...)):
    try:
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional summarizer. Return clean, clear summaries without prefacing or disclaimers.",
                },
                {"role": "user", "content": text},
            ],
            temperature=0.5,
        )
        summary = response.choices[0].message.content.strip()
        return {"summary": summary}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# === Placeholder Tools ===
@app.get("/bills", response_class=HTMLResponse)
def bills_placeholder(request: Request):
    return templates.TemplateResponse("placeholder.html", {"request": request, "tool": "Bills Sheet"})

@app.get("/weather", response_class=HTMLResponse)
def weather_placeholder(request: Request):
    return templates.TemplateResponse("placeholder.html", {"request": request, "tool": "Weather Tool"})

@app.get("/monster", response_class=HTMLResponse)
def monster_placeholder(request: Request):
    return templates.TemplateResponse("placeholder.html", {"request": request, "tool": "Monster Generator"})
