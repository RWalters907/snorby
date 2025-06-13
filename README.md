# Snorby.net 💤 — BASE BUILD

A cuddly, friendly FastAPI web app for family tools, automation, and fun — with a sleepy mascot named Snorby.

---

## 🛠 Requirements

- Python 3.10 or later
- All dependencies listed in `requirements.txt`
- Transparent PNGs and full favicon set included
- Project tested using modern browsers for compatibility
- `.env` file required with `OPENAI_API_KEY` for summarizer tool

---

## 🚀 Setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the root directory with:

```env
OPENAI_API_KEY=your-openai-api-key-here
```

---

## ▶️ Run the App

```bash
uvicorn app.main:app --reload
```

Then open your browser to:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Project Structure

```
snorby/
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── templates/
│   │   ├── layout.html
│   │   ├── index.html
│   │   ├── smart_summarizer.html
│   │   ├── get_weather.html
│   │   ├── monster.html
│   │   └── bills_sheet.html
│   └── static/
│       ├── style.css
│       ├── script.js
│       ├── js/
│       │   └── main.js
│       ├── images/
│       │   └── Snorby.png
│       └── favicon/
│           ├── favicon.ico
│           ├── apple-touch-icon.png
│           ├── android-chrome-192x192.png
│           ├── android-chrome-512x512.png
│           ├── site.webmanifest
│           └── ...
├── requirements.txt
├── .env
└── README.md
```

---

## 🧠 Smart Summarizer Integration

The Smart Summarizer is now fully integrated into Snorby as a standalone page powered by the OpenAI API.

- Visit: `http://127.0.0.1:8000/smart_summarizer`
- Enter/paste any long text
- Press the “Summarize” button
- The result will appear in a styled box below

### Key Files

- `app/templates/smart_summarizer.html` — HTML frontend
- `app/static/script.js` — Handles the form POST
- `/summarize` route in `main.py` — Calls OpenAI's API

### Behavior

- FastAPI backend uses the OpenAI Python SDK
- Prompts GPT-3.5 with clean summarization instructions
- Response is stripped of disclaimers or AI-flavored phrasing

---

## 💡 Notes

- `Snorby.png` has a transparent background for seamless design  
- All favicon variants are placed in `static/favicon/`  
- All tools use modular routing via `app/routes.py`  
- Templates extend from `layout.html` and inherit styling  
- Font: [Google Fonts - Poppins](https://fonts.google.com/specimen/Poppins)  
- Icons via [Font Awesome 6](https://fontawesome.com/icons)

---

## 🔁 Restore From Backup

To restore this build:

```bash
unzip snorby_base_build.zip
cd snorby_base_build
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

Enjoy Snorby 💤 – RW

