from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .scraper import fetch_html
from .diff import compare_html
from .auditor import run_pa11y
from .db import save_result, init_db

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

init_db()

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.post("/submit/")
def submit_url(url: str = Form(...)):
    html = fetch_html(url)
    diff = compare_html(url, html)
    audit = run_pa11y(url)
    save_result(url, html, diff, audit)
    return {"status": "ok"}
