from fastapi import FastAPI, Form, Request

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app= FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "Name":"Joel"})

@app.post("/login")
def dashboard(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == "admin@admin.com" and password == "password":
        @app.get("/dashboard")
        def dashboard(request: Request):
            return templates.TemplateResponse("dashboard.html", {"request": request, "Name":"Joel"})
        
    elif username == "student@student.com" and password == "password":
        @app.get("/student_dashboard")
        def student_dashboard(request: Request):
            return templates.TemplateResponse("student_dashboard.html", {"request": request, "Name":"Joel"})
    else:
        return templates.TemplateResponse("index.html", {"request": request, "Name":"Joel", "error": "Invalid credentials"})