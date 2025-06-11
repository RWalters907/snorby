from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head><title>Snorby</title></head>
        <body style='font-family:sans-serif;text-align:center;margin-top:50px;'>
            <h1>Welcome to Snorby.net 💤</h1>
            <p>Your cuddly, friendly home for family tools and silly fun.</p>
        </body>
    </html>
    """

@app.get("/api/monster")
async def get_monster_name():
    names = [
        "Grubblefuzz", "Snorgle", "Wibblenub", "Flarble", "Zumble", 
        "Mibber", "Flonky", "Snorby", "Plobber", "Tibbo"
    ]
    return {"monster": random.choice(names)}
