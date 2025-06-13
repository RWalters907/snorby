from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/summarizer", response_class=HTMLResponse)
async def smart_summarizer_page(request: Request):
    return templates.TemplateResponse("summarizer.html", {"request": request})
