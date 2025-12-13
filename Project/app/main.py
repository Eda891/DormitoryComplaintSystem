from fastapi import FastAPI
from routers import auth, complaints, categories, admin
from database import create_db_tables
app = FastAPI(title="Dormitory Complaint System")

create_db_tables()

app.include_router(auth.router,      prefix="/auth",      tags=["auth"])
app.include_router(complaints.router,prefix="/complaints",tags=["complaints"])
app.include_router(categories.router, prefix="/categories", tags=["categories"])
app.include_router(admin.router,     prefix="/admin",     tags=["admin"])

@app.get("/")
def home():
    return {"message": "Dorm Complaint System Backend Running ✅"}
