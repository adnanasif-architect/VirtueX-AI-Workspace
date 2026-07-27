from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


class LeadData(BaseModel):
    budget: int


@app.get("/")
def home():
    return FileResponse("index.html")


@app.post("/check-lead")
def process_lead(data: LeadData):
    budget = data.budget

    if budget >= 5000:
        result = "VIP Lead"
    elif budget >= 500:
        result = "high value lead"
    else:
        result = "low value lead"

    return {"status": "success", "lead_type": result}
