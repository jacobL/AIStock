from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}
#uvicorn index:app --host 127.0.0.1 --port 81 --reload
