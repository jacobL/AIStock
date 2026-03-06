from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# 指定 templates 目錄
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    
    data = {
        "message": "Hello FastAPI",
        "name": "Jacob"
    }

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "data": data
        }
    )
#uvicorn index:app --host 127.0.0.1 --port 81 --reload
