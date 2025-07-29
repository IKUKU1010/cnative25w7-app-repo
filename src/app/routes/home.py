from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")

# Dictionary to hold votes
votes = {
    "Arsenal": 0,
    "Chelsea": 0,
    "Liverpool": 0,
    "Manchester City": 0,
    "Manchester United": 0,
    "Tottenham": 0
}

@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "votes": votes})

@router.post("/vote", response_class=HTMLResponse)
def vote(request: Request, team: str = Form(...)):
    if team in votes:
        votes[team] += 1
    return templates.TemplateResponse("index.html", {"request": request, "votes": votes})
