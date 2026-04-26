from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Golf AI OK"}

@app.get("/golf")
def golf():
    print("✅ Golf AI : requête reçue !")
    return {"status": "reçu"}