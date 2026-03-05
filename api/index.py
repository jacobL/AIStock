from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}
#uvicorn index:app --host 127.0.0.1 --port 81 --reload