from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app import routes

app = FastAPI()

# Mount static files (CSS, JS, images, etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include all your page routes
app.include_router(routes.router)
