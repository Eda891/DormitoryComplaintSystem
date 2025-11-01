from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Dorm Complaint System Backend Running ✅"}
