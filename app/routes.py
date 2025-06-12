from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/smart_summarizer", response_class=HTMLResponse)
async def smart_summarizer(request: Request):
    return templates.TemplateResponse("smart_summarizer.html", {"request": request})

@router.get("/bills_sheet", response_class=HTMLResponse)
async def bills_sheet(request: Request):
    return templates.TemplateResponse("bills_sheet.html", {"request": request})

@router.get("/get_weather", response_class=HTMLResponse)
async def get_weather(request: Request):
    return templates.TemplateResponse("get_weather.html", {"request": request})

@router.get("/monster", response_class=HTMLResponse)
async def monster(request: Request):
    return templates.TemplateResponse("monster.html", {"request": request})
