from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class GolfRequest(BaseModel):
    action: str

@app.post("/golf")
def golf(req: GolfRequest):
    print("📩 ACTION:", req.action)
    return {"status": "ok"}