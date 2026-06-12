from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

@app.get("/about")
def about():
    return {"name": "Karthik", "role": "AI & ML Student"}

@app.get("/add")
def add(a: int, b: int):
    return {"sum": a + b}
