from fastapi import FastAPI, Form, Request

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

cars = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2020},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2019},
    {"id": 3, "make": "Ford", "model": "Mustang", "year": 2021}]



app= FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "Name":"Joel"})

@app.get("/dashboard_blueprint")
def dashboard(request: Request):
    return templates.TemplateResponse("layout.html", {"request": request, "Name":"Joel"})

@app.get("/data")
def dashboard(request: Request):
    return templates.TemplateResponse("data.html", {"request": request, "Name":"Letisha", "cars":cars})

@app.post("/login")
def login(request: Request, name: str = Form(...), password: str = Form(...)):
    if name == "admin@admin.com" and password == "password":
       
            return templates.TemplateResponse("dashboard.html", {"request": request, "Name":"Joel"})
        
    elif name == "student@student.com" and password == "password":
       
            return templates.TemplateResponse("student_dashboard.html", {"request": request, "Name":"Joel"})
    else:
        return templates.TemplateResponse("index.html", {"request": request, "Name":"Joel", "error": "Invalid credentials"})